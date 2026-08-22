# Collaboration and Agent-Orchestration Protocol

FaultAdapt-Gym is a collaboration with Chathuka—not an autonomous research project run by AI.

## Decision ownership

Chathuka owns:

- the research question and hypotheses;
- final paper selection and interpretation;
- methodological choices after reviewing alternatives;
- experiments treated as evidence;
- claims, writing voice, outreach, and submission decisions.

Fabric acts as project lead and orchestrator. It maintains the roadmap, identifies dependencies, prepares decision points, tracks evidence, coordinates specialist agents, and verifies engineering artifacts. It must not silently replace Chathuka's learning or judgment.

## Agent roles

### Research bot

Use a dedicated delegated agent/session for literature work:

- search for papers and official implementations;
- produce structured paper matrices;
- trace prior work and competing benchmarks;
- identify possible gaps and contradictory evidence;
- return citations, links, confidence, and unresolved questions.

It does not choose the research claim. Chathuka reviews the output and records what he understands, disagrees with, and wants to test.

### Experiment bot

Use a separate agent/session for bounded engineering subtasks:

- inspect relevant repository code;
- propose experiment configurations;
- implement an approved, narrowly scoped component;
- run tests and return real logs and artifact paths.

It must not expand the experiment matrix without approval.

### Reviewer bot

Use an independent agent/session after a proposal, protocol, or result exists:

- look for leakage, unfair comparisons, confounders, and missing baselines;
- challenge statistical and causal claims;
- distinguish infrastructure success from scientific evidence;
- produce blocking issues and optional improvements separately.

### Writing bot

Use only after Chathuka records his interpretation:

- organize notes into a report section;
- improve clarity without inventing claims;
- maintain citation and evidence links;
- mark unresolved placeholders explicitly.

## Workflow for every research subgoal

1. **Frame together:** Fabric presents the decision, constraints, and two or three viable options.
2. **Choose:** Chathuka selects or revises the question and states his current reasoning.
3. **Delegate:** Fabric gives the specialist bot a bounded, self-contained brief.
4. **Inspect:** The bot returns sources, artifacts, uncertainty, and open questions—not a final decision.
5. **Discuss:** Fabric summarizes trade-offs and asks Chathuka to interpret the evidence.
6. **Decide:** Chathuka approves the method, claim, or next experiment.
7. **Execute:** An experiment bot or Fabric implements only the approved scope.
8. **Review independently:** A reviewer bot checks the result before it enters the paper.
9. **Record:** Fabric updates the board and research log with decisions and verifiable evidence.

## Required agent handoff

Every delegated brief should include:

- **Subgoal:** one concrete question or artifact;
- **Context:** relevant repository paths and prior decisions;
- **Inputs:** papers, code, data, or experiment outputs it may use;
- **Constraints:** compute, hardware, time, and excluded work;
- **Deliverable:** exact format and acceptance criteria;
- **Evidence:** URLs, commands, logs, or file paths;
- **Uncertainty:** assumptions and unresolved issues;
- **Non-goals:** decisions the agent is not allowed to make.

## Session boundaries

Use separate sessions or delegated agents for literature review, implementation, methodological review, and writing so their assumptions do not collapse into one voice. Fabric remains the main planning session and synthesizes their outputs. Agent self-reports are treated as unverified until source links, files, or execution results are checked.

## Current division of work

For Week 1:

- **Chathuka:** confirm available weekly hours, write his own short motivation for the research question, and review the four hypotheses in `ROADMAP.md`.
- **Fabric:** maintain the plan, prepare decision points, track deliverables, and coordinate agents.
- **Research bot:** begins only after Chathuka chooses the first literature question.
- **Experiment bot:** handles bounded implementation after the experiment design is approved.
- **Reviewer bot:** reviews the Week 4 proposal before the environment and method scope are frozen.
