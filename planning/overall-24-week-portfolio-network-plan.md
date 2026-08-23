# 24-Week Overall Robotics Career Plan

## Discord thread opening

Hi! I am Chathuka Elapatha, a third-year Electronic and Telecommunication Engineering undergraduate at the University of Moratuwa. My long-term goal is graduate study and research or engineering work in robotics, reinforcement learning, and embodied AI.

I already have strong engineering foundations—a 3.99/4.00 CGPA, an industrial vision-and-SCARA glove-inspection system, BLDC/FOC motor-control work, ROS/ROS 2 and embedded experience, and robotics teaching/competition involvement—but I need stronger evidence in robot learning research, a clearer public portfolio, and meaningful academic/industry relationships.

This 24-week plan combines four tracks:

1. one rigorous robot-learning research project;
2. conversion of existing engineering work into polished public case studies;
3. evidence-first relationship building with academics and industry engineers;
4. preparation for internships, research roles, and future higher-study applications.

The aim is not to collect connections or force a publication. It is to become someone whose public work makes good researchers and engineers willing to engage.

**Flagship project:** FaultAdapt-Gym — https://github.com/Chippy1520/faultadapt-gym

I would appreciate feedback on scope, sequencing, and the kind of evidence that would make me competitive for future research or robotics-industry opportunities.

---

## End state after 24 weeks

### Portfolio

- One research-grade flagship: FaultAdapt-Gym.
- One polished industrial case study: vision-guided SCARA glove inspection.
- One polished controls/embedded case study: BLDC/FOC motor drive, with a ROS/robotics supporting-work section.
- A compact personal portfolio, cleaned GitHub profile, 2–4 minute demos, and concise technical write-ups.

### Research

- A reproducible repository, literature matrix, controlled experiments, and 6–8 page technical report.
- A mentor-reviewed decision on workshop, undergraduate symposium, preprint, or further experiments.
- Honest negative results and limitations rather than unsupported novelty claims.

### Relationships

- Two thoughtful technical interactions per week.
- One short-conversation invitation every two weeks.
- Approximately 4–8 meaningful conversations and 2–4 continuing relationships as a realistic target.
- Relationships built first with UoM lecturers, postgraduate researchers, alumni, maintainers, and first authors—not only famous PIs.

### Career preparation

- Separate academic CV and robotics-industry résumé.
- A one-page research summary and project one-pager.
- A spreadsheet of 8–12 well-matched laboratories and 10–15 realistic organizations/programs.
- At least one mock research interview and one robotics/software interview.

## Weekly workload

Target: **12–15 hours per week**.

- 5–7 h flagship implementation and experiments
- 2 h focused learning tied to the project
- 2 h paper reading and research notes
- 1.5–2 h portfolio and technical communication
- 1–1.5 h relationship building and applications

During examinations, reduce to eight hours but preserve one visible weekly artifact.

---

# 24-week plan

## Phase 1 — Positioning and foundations: Weeks 1–4

### Week 1 — Personal audit and system setup

**Research/project**
- Freeze the flagship problem, available compute, weekly schedule, and minimum viable result.
- Run the current FaultAdapt-Gym smoke experiment and record the starting point.

**Portfolio**
- Audit LinkedIn, GitHub, CV, and all previous projects.
- Select three stories: FaultAdapt-Gym, SCARA inspection, and BLDC/FOC control.

**Relationships/career**
- Build a tracker with 20 initial people: UoM faculty, postgraduate students, alumni, industry engineers, maintainers, and the five scouted contacts.
- Identify 10 people reachable through existing UoM connections.

**Deliverable:** one-page strengths/gaps audit, weekly calendar, and relationship tracker.

### Week 2 — Improve professional positioning

**Research/project**
- Reproduce a seeded control/RL baseline and lock the local environment.

**Portfolio**
- Rewrite the LinkedIn headline/about section around robotics, controls, and robot learning.
- Create an academic CV and industry résumé draft.
- Clean GitHub profile, descriptions, pinned repositories, and READMEs.

**Relationships/career**
- Join 2–3 useful communities: UoM robotics/AI, IEEE/IES/RAS, ROS, or relevant open-source communities.
- Introduce yourself only where context makes it appropriate.

**Deliverable:** credible LinkedIn, two CV variants, and cleaned GitHub front page.

### Week 3 — Research map and local network map

**Research/project**
- Read five anchor papers and build a literature/duplication table.

**Portfolio**
- Draft the SCARA case-study structure: problem, system architecture, personal contribution, metrics, deployment constraints, and evidence that can be disclosed.

**Relationships/career**
- Study five UoM or Sri Lankan researchers in controls, robotics, vision, or ML.
- Record one recent project/paper and one legitimate question for each.

**Deliverable:** literature matrix, local mentor shortlist, and SCARA case-study outline.

### Week 4 — Proposal review and first mentor relationship

**Research/project**
- Write a two-page FaultAdapt-Gym proposal with question, hypotheses, baselines, metrics, compute cap, and risks.

**Portfolio**
- Prepare a 60-second personal introduction and two-minute flagship explanation.

**Relationships/career**
- Ask one lecturer or postgraduate researcher for a 20-minute proposal critique.
- Send the proposal and three bounded questions; do not ask vaguely for mentorship.

**Gate:** proceed only if the project runs locally, has measurable variables, and can produce a report without GPU or hardware.

---

## Phase 2 — Produce visible evidence: Weeks 5–8

### Week 5 — Public project foundation

- Make the flagship repository reproducible: setup, tests, license, roadmap, issue tracker, and experiment logging.
- Publish a restrained kickoff post explaining the question and constraints without claiming novelty.
- Start the public SCARA case-study page using only non-confidential material.

**Deliverable:** public research repository and first portfolio case-study draft.

### Week 6 — First baseline and first technical interaction

- Implement and evaluate the classical/non-learning baseline.
- Produce the first metrics table and one honest failure example.
- Ask a relevant senior, alumnus, or controls researcher one specific methodological question.
- Study Scott Nguyen’s public controls/robotics portfolio as a model for communicating engineering depth; engage only if a genuine technical question emerges.

**Deliverable:** baseline result plus one useful technical conversation or unanswered-but-well-formed outreach attempt.

### Week 7 — Evaluation infrastructure and communication practice

- Add fixed evaluation conditions, seeds, configurations, metrics, and automatic result export.
- Record a private two-minute walkthrough and test it with a peer unfamiliar with the project.
- Improve the SCARA diagrams and quantify cycle time, accuracy, reliability, or deployment outcomes where disclosure is allowed.

**Deliverable:** reproducible evaluation harness and understandable project explanation.

### Week 8 — First learning baseline and mentor update

- Implement a standard feed-forward PPO baseline before any novel method.
- Send the Week-4 reviewer a one-page progress update containing results, failures, and one question.
- Publish technical update #1 with a plot, code link, and limitation.

**Gate:** at least two baselines run end-to-end, metrics are automatic, and a clean installation passes a smoke test.

---

## Phase 3 — Build depth and contribution: Weeks 9–12

### Week 9 — Controlled research factor

- Add one controlled factor: hidden actuator degradation, latency, or another frozen scope element.
- Run a small pilot comparison.
- Leave one substantive issue/discussion/comment in a relevant open-source project only if it adds reproducible information.

### Week 10 — Narrow contribution and informational conversation

- Implement one narrowly defined adaptation/decision mechanism.
- Conduct one short conversation with an alumnus, postgraduate student, or robotics engineer about real work, evidence expected, and skills gaps.
- Do not ask for a job; ask how systems are evaluated and deployed.

### Week 11 — Ablation and public writing

- Run one ablation or controlled parameter study with uncertainty/error bars.
- Publish a short note explaining one result or failed hypothesis.
- Draft the BLDC/FOC case study with control architecture, hardware constraints, test method, and your specific contribution.

### Week 12 — Midpoint demo and portfolio release

- Produce a midpoint demo and one-page continue/simplify/pivot memo.
- Present it to a lecturer, lab group, club, or 2–3 technical peers and record feedback.
- Release portfolio v1 containing the SCARA and motor-control case studies plus the live research project.

**Gate:** continue the research claim only if the pipeline is reliable and the factor produces measurable behavior. Otherwise present it honestly as an engineering benchmark.

---

## Phase 4 — Rigor and targeted network development: Weeks 13–16

### Week 13 — Final experiment design and laboratory map

- Freeze primary baselines and metrics; add realism only if it does not destabilize the project.
- Build a spreadsheet of 8–12 international labs based on research fit rather than ranking.
- For each lab record two papers, fit, missing skills, degree route, funding route, deadlines, and relevant students.

### Week 14 — Repeated trials and author/student contact

- Run repeated trials with at least three seeds where affordable and log runtime/hardware.
- Contact one first author, research student, or maintainer whose work directly affected the experiment.
- Include a reproduced result or artifact and one answerable question.

### Week 15 — Error analysis and research-fit writing

- Categorize failures, inspect trajectories, and check leakage or unfair baselines.
- Write a one-page research-fit note connecting the project to two target laboratories.
- Identify concrete gaps to close before graduate applications.

### Week 16 — Freeze features and obtain external review

- Complete final ablations/generalization tests; stop feature development except for correctness bugs.
- Ask a technically qualified reviewer to inspect the repository, method, and central plot.
- Study Benjamin Swilling’s fault-tolerant locomotion themes and Chris Bentzel’s production robot-software/testing perspective. Contact only if the now-mature artifact supports a specific question.

**Deliverable:** reviewer feedback log and frozen experiment scope.

---

## Phase 5 — Report, portfolio, and credibility: Weeks 17–20

### Week 17 — Results and evidence-focused CV

- Regenerate all figures from saved logs and draft methods/results.
- Rewrite both CVs around evidence: metrics, decisions, reproducibility, individual contribution, and links.
- Remove generic skill lists that are not supported by projects.

### Week 18 — Complete report and obtain two reviews

- Write introduction, related work, limitations, and conclusion to create a 6–8 page internal report.
- Request one technical review and one communication/writing review with a clear deadline.
- Practice a ten-minute research talk.

### Week 19 — Reproducibility and higher-study packet

- Address review comments and add a reproducibility checklist, citation file, runtimes, and one-command evaluation where practical.
- Prepare transcript, academic CV, one-page research-interest statement, laboratory spreadsheet, and referee shortlist.

### Week 20 — Release the complete public artifact

- Release repository v1.0, report, project page, and a 2–4 minute demo with limitations and negative results.
- Publish portfolio v2 and update LinkedIn/GitHub.
- Personally thank everyone who gave feedback and state what changed because of it.

**Publication gate:** submit only after experienced review, credible baselines, repeated trials, and venue-fit checking. A strong report is better than a weak or predatory publication.

---

## Phase 6 — Convert evidence into opportunities: Weeks 21–24

### Week 21 — Personalized outreach

- Package one reusable component from the project with tests and examples.
- Send 3–4 highly personalized messages across academic and industry targets.
- Each message must reference actual work, show a relevant artifact, and ask one precise question.
- Do not message all five scouted people simply to meet a weekly quota.

### Week 22 — Open-source contribution and interview practice

- Submit one useful documentation fix, test, issue reproduction, or scoped pull request to a project used in the research.
- Complete one mock research interview and one robotics/software interview.
- Practice explaining failures and your personal contribution, not only final results.

### Week 23 — Applications and publication decision

- Decide with a mentor whether the report should become a workshop/student-symposium submission, preprint, extended study, or remain a technical report.
- Apply selectively to suitable research assistantships, internships, summer programs, labs, and robotics roles.
- Tailor each application around demonstrated fit.

### Week 24 — Retrospective and durable relationships

- Record lessons, unresolved defects, experiment costs, and next questions.
- Create a six-month continuation plan tied to graduation and application cycles.
- Follow up once with key contacts; stop after one polite follow-up if there is no response.
- Request a recommendation only from someone who has actually reviewed or observed the work.

**Final deliverable:** portfolio v2, flagship v1.0, report/demo, application packet, relationship map, and next six-month plan.

---

# Relationship-building strategy

## Priority order

1. UoM lecturers and postgraduate researchers.
2. UoM and Sri Lankan alumni in robotics/ML.
3. Open-source maintainers and first authors directly related to the flagship.
4. Accessible industry engineers and research students.
5. Senior academics and industry leaders after a relevant artifact exists.

## Five scouted contacts

- **Scott Nguyen:** accessible engineering/controls portfolio model; potential near-peer industry conversation after a concrete controls or calibration question.
- **Benjamin Swilling:** fault tolerance, locomotion, recovery, and deployed legged systems; approach after producing fault-adaptation results or a recovery-focused demo.
- **Chris Bentzel:** production robot-software architecture, simulation, observability, and RL-policy deployment; approach with a tested debugging/fault-injection artifact.
- **Yuke Zhu:** robot learning, simulation, AMAGO, RoboCasa, and generalist embodied agents; engage first through papers, repositories, students, or maintainers and use official routes for formal opportunities.
- **Chelsea Finn:** meta-learning, robot learning, adaptation, and generalist policies; do not send a generic joining request. Build a substantial artifact, engage the relevant paper/code ecosystem, and respect IRIS’s formal contact policy.

## Outreach template

> I’m a third-year University of Moratuwa undergraduate working on [specific problem]. Your [paper/project/patent/talk] changed how I approached [specific decision]. I reproduced/implemented [artifact] and observed [concrete result or limitation]. The code and short result are here: [link]. Would [small technical question] be the right way to evaluate or improve this aspect?

Avoid résumé-first messages, mass outreach, vague requests for mentorship, and asking famous PIs for positions before producing relevant evidence.

---

# Six scorecards

Review these at Weeks 4, 8, 12, 16, 20, and 24.

## Portfolio

- Three polished case studies.
- Clear personal contribution and quantitative evidence.
- Short demo for each major project.
- Compact portfolio and clean pinned repositories.

## Research

- Explicit question and baselines.
- Reproducible environment, configs, seeds, and tests.
- Ablation, robustness/generalization test, and failure analysis.
- Honest limitations and externally reviewed report.

## Relationships

- Two thoughtful interactions per week.
- One conversation invitation every two weeks.
- Interactions tracked as aware / interacted / advised / collaborated.
- Target 4–8 meaningful conversations and 2–4 continuing relationships—not a connection count.

## Communication

- 30-second, two-minute, and ten-minute explanations.
- Six monthly public technical updates.
- One presentation, one report, and one project one-pager.

## Higher studies

- 8–12 fit-based labs with funding and deadline information.
- Academic CV, transcript, research-interest statement, and referee plan.
- Recommendations developed through observed work.

## Industry readiness

- Industry résumé and evidence of software quality, controls, testing, deployment, and debugging.
- One open-source contribution.
- One mock technical interview and one mock project/research discussion.

## Definition of success

Success after 24 weeks is not “Chelsea Finn replied” or “a paper was accepted.” Success is having undeniable evidence of sustained technical and research ability, a coherent public story connecting industrial robotics to robot learning, mentors who know the work, and a repeatable system for creating relevant relationships and opportunities before graduation.
