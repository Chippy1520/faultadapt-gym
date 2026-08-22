# Research Collaboration Protocol

FaultAdapt-Gym is a student-led research collaboration—not an autonomous agent project.

## Roles

### Student researcher (Chathuka)

- Owns the research question, hypotheses, and final claims.
- Reads the shortlisted anchor papers rather than relying only on summaries.
- Chooses methods after reviewing trade-offs.
- Runs or directly reviews key experiments.
- Writes the first interpretation of important results.
- Approves protocol freezes, scope changes, public releases, and submissions.

### Main Fabric session — coordinator

- Maintains the 24-week plan, dependencies, board, and stage gates.
- Decomposes weekly goals into bounded research, engineering, and review tasks.
- Assigns specialist agents only the context they need.
- Integrates agent outputs into options and evidence packets.
- Checks citations, reproducibility, scope, and unsupported claims.
- Never substitutes agent-generated conclusions for the student's judgment.

### Research bot / literature agents

- Locate primary papers, official code, datasets, and benchmarks.
- Build evidence tables and identify conflicting findings.
- Extract limitations and open questions with source links.
- Flag possible duplication and uncertainty.
- Do not decide novelty, hypotheses, interpretations, or paper claims.

### Engineering / experiment agents

- Implement bounded components, tests, configurations, and analysis tools.
- Return exact commands, artifacts, and observed results.
- Do not expand the experimental scope or launch expensive sweeps without approval.

### Reviewer agents

- Critique a proposal, protocol, code path, figure, or draft independently.
- Look for confounds, leakage, weak baselines, and overclaiming.
- Do not silently rewrite the student's scientific position.

## Session map

The main session remains the control room. Separate delegated sessions are created for:

1. Adaptive/meta-RL literature scouting.
2. Benchmark and novelty landscape checking.
3. CPU-feasible methods and implementation scouting.
4. Individual engineering components when implementation begins.
5. Independent experiment/protocol review.
6. Paper review near release.

Each sub-session receives a bounded question and returns an evidence packet to the main session. Decisions are made here with the student.

## Collaboration loop

1. **Frame:** Main session and student define the question and acceptance criteria.
2. **Delegate:** Specialist agent investigates one bounded subgoal.
3. **Inspect:** Main session checks sources, assumptions, and missing evidence.
4. **Discuss:** Student reviews options and explains their preferred interpretation.
5. **Decide:** Student approves the method, hypothesis, or scope change.
6. **Execute:** Student and engineering agent implement/run the agreed work.
7. **Interpret:** Student writes the first result interpretation; agents critique it.
8. **Record:** Commit artifacts and update the research log and project board.

## Required student approval gates

No agent may silently pass these gates:

- final research-question selection;
- anchor-paper shortlist;
- two-page proposal;
- baseline and metric selection;
- final evaluation protocol;
- interpretation of headline results;
- novelty wording;
- public release or venue submission.

## Agent output contract

Every research packet must contain:

- bounded question answered;
- primary-source links;
- evidence versus inference clearly separated;
- limitations and contradictory evidence;
- decisions still required from the student;
- suggested next reading or experiment;
- no fabricated citations, results, or novelty claims.

## Current delegated research work

The first parallel research cycle covers:

- adaptive/meta-RL under hidden and changing faults;
- related benchmarks and possible duplication;
- practical CPU-first baseline implementations.

The outputs are inputs to a student discussion—not a finished literature review or autonomous research decision.
