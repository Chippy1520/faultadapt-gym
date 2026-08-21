#!/usr/bin/env python3
"""Populate GitHub Issues and Project fields from planning/board-import.csv.

Requires an authenticated GitHub CLI with repo and project scopes.
The script is idempotent by exact issue title: reruns reuse existing issues.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import subprocess
import time
from pathlib import Path

OWNER = "Chippy1520"
REPO = f"{OWNER}/faultadapt-gym"
PROJECT_NUMBER = "3"
GH = r"C:\Program Files\GitHub CLI\gh.exe"
CSV_PATH = Path(__file__).with_name("board-import.csv")
PROJECT_ID = "PVT_kwHOBZguQs4BhEM0"
FIELD_IDS = {
    "Status": "PVTSSF_lAHOBZguQs4BhEM0zhgBYu8",
    "Week": "PVTF_lAHOBZguQs4BhEM0zhgBZC0",
    "Phase": "PVTSSF_lAHOBZguQs4BhEM0zhgBZC4",
    "Start date": "PVTF_lAHOBZguQs4BhEM0zhgBZC8",
    "Target date": "PVTF_lAHOBZguQs4BhEM0zhgBZDA",
}
STATUS_OPTIONS = {"Todo": "f75ad846", "In Progress": "47fc9ee4", "Done": "98236657"}
PHASE_OPTIONS = {
    "1 — Foundations": "24027219",
    "2 — Infrastructure": "dc91e207",
    "3 — Research contribution": "2f4b2b28",
    "4 — Final experiments": "d82149da",
    "5 — Paper and release": "e3994753",
    "6 — Outreach and career package": "e706e48d",
}


def run(*args: str) -> str:
    last_error: subprocess.CalledProcessError | None = None
    for attempt in range(1, 6):
        try:
            proc = subprocess.run(
                [GH, *args], check=True, text=True, capture_output=True, encoding="utf-8"
            )
            return proc.stdout.strip()
        except subprocess.CalledProcessError as exc:
            last_error = exc
            if attempt == 5:
                break
            time.sleep(2**attempt)
    assert last_error is not None
    raise RuntimeError(
        f"GitHub CLI failed after 5 attempts: {' '.join(args)}\n"
        f"stdout: {last_error.stdout}\nstderr: {last_error.stderr}"
    ) from last_error


def ensure_label() -> None:
    run(
        "label",
        "create",
        "roadmap",
        "--repo",
        REPO,
        "--color",
        "1D76DB",
        "--description",
        "A scheduled task in the 24-week research roadmap",
        "--force",
    )


def existing_issues() -> dict[int, dict[str, object]]:
    raw = run("api", f"repos/{REPO}/issues?state=all&per_page=100")
    issues: dict[int, dict[str, object]] = {}
    for item in json.loads(raw):
        if "pull_request" in item:
            continue
        match = re.match(r"Week\s+(\d{1,2}):", item["title"])
        if not match:
            continue
        issues[int(match.group(1))] = {
            "url": item["html_url"],
            "id": item["node_id"],
            "number": item["number"],
        }
    return issues


def issue_body(row: dict[str, str]) -> str:
    return f"""## Technical / research work

{row['Technical / research work']}

## Exit criterion

- [ ] {row['Exit criterion']}

## Relationship / public action

- [ ] {row['Relationship / public action']}

## Schedule

- **Week:** {row['Week']} of 24
- **Phase:** {row['Phase']}
- **Start:** {row['Start date']}
- **Target:** {row['Target date']}

## Completion evidence

Before closing, link the relevant commit, plot, report, demo, issue/PR, meeting note, or other verifiable artifact here.
"""


def graphql(query: str) -> dict[str, object]:
    return json.loads(run("api", "graphql", "-f", f"query={query}"))["data"]


def existing_project_items() -> dict[str, str]:
    query = f'''query {{
      node(id: "{PROJECT_ID}") {{
        ... on ProjectV2 {{
          items(first: 100) {{
            nodes {{ id content {{ ... on Issue {{ id }} }} }}
          }}
        }}
      }}
    }}'''
    nodes = graphql(query)["node"]["items"]["nodes"]
    return {
        node["content"]["id"]: node["id"]
        for node in nodes
        if node.get("content") and node["content"].get("id")
    }


def add_project_item(issue_id: str) -> str:
    query = f'''mutation {{
      addProjectV2ItemById(input: {{projectId: "{PROJECT_ID}", contentId: "{issue_id}"}}) {{
        item {{ id }}
      }}
    }}'''
    return graphql(query)["addProjectV2ItemById"]["item"]["id"]


def configure_project_item(item_id: str, row: dict[str, str]) -> None:
    status = "In Progress" if row["Week"] == "1" else "Todo"
    query = f'''mutation {{
      week: updateProjectV2ItemFieldValue(input: {{projectId: "{PROJECT_ID}", itemId: "{item_id}", fieldId: "{FIELD_IDS['Week']}", value: {{number: {row['Week']}}}}}) {{ projectV2Item {{ id }} }}
      phase: updateProjectV2ItemFieldValue(input: {{projectId: "{PROJECT_ID}", itemId: "{item_id}", fieldId: "{FIELD_IDS['Phase']}", value: {{singleSelectOptionId: "{PHASE_OPTIONS[row['Phase']]}"}}}}) {{ projectV2Item {{ id }} }}
      start: updateProjectV2ItemFieldValue(input: {{projectId: "{PROJECT_ID}", itemId: "{item_id}", fieldId: "{FIELD_IDS['Start date']}", value: {{date: "{row['Start date']}"}}}}) {{ projectV2Item {{ id }} }}
      target: updateProjectV2ItemFieldValue(input: {{projectId: "{PROJECT_ID}", itemId: "{item_id}", fieldId: "{FIELD_IDS['Target date']}", value: {{date: "{row['Target date']}"}}}}) {{ projectV2Item {{ id }} }}
      status: updateProjectV2ItemFieldValue(input: {{projectId: "{PROJECT_ID}", itemId: "{item_id}", fieldId: "{FIELD_IDS['Status']}", value: {{singleSelectOptionId: "{STATUS_OPTIONS[status]}"}}}}) {{ projectV2Item {{ id }} }}
    }}'''
    graphql(query)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--start-week",
        type=int,
        default=1,
        help="First weekly item to configure; useful when resuming after an API interruption.",
    )
    parser.add_argument(
        "--issues-only",
        action="store_true",
        help="Create missing issues using REST but defer Project fields.",
    )
    args = parser.parse_args()
    ensure_label()
    known = existing_issues()
    with CSV_PATH.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    if len(rows) != 24:
        raise RuntimeError(f"Expected 24 weekly rows, found {len(rows)}")
    project_items = {} if args.issues_only else existing_project_items()

    created = 0
    for row in rows:
        if int(row["Week"]) < args.start_week:
            continue
        week = int(row["Week"])
        title = row["Title"]
        body = issue_body(row)
        record = known.get(week)
        if not record:
            response = run(
                "api",
                "--method",
                "POST",
                f"repos/{REPO}/issues",
                "-f",
                f"title={title}",
                "-f",
                f"body={body}",
                "-f",
                "labels[]=roadmap",
                "-f",
                f"assignees[]={OWNER}",
            )
            issue = json.loads(response)
            record = {
                "url": issue["html_url"],
                "id": issue["node_id"],
                "number": issue["number"],
            }
            known[week] = record
            created += 1
        else:
            run(
                "api",
                "--method",
                "PATCH",
                f"repos/{REPO}/issues/{record['number']}",
                "-f",
                f"title={title}",
                "-f",
                f"body={body}",
                "-f",
                "labels[]=roadmap",
                "-f",
                f"assignees[]={OWNER}",
            )

        url = str(record["url"])
        issue_id = str(record["id"])

        if args.issues_only:
            print(f"Ensured week {int(row['Week']):02d}: {url}")
            continue

        item_id = project_items.get(issue_id)
        if not item_id:
            item_id = add_project_item(issue_id)
            project_items[issue_id] = item_id
        configure_project_item(item_id, row)
        print(f"Configured week {int(row['Week']):02d}: {url}")

    selected = sum(int(row["Week"]) >= args.start_week for row in rows)
    if args.issues_only:
        print(f"Done: {created} issues created, {selected} weekly issues ensured; Project fields deferred.")
    else:
        print(f"Done: {created} issues created, {selected} project items configured.")


if __name__ == "__main__":
    main()
