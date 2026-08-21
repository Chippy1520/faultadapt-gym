# Chathuka Elapatha — 24-Week Robotics, RL & Embodied-AI Roadmap

**Planning assumption:** 12–15 focused hours/week alongside university work. During exams, use the 6-hour minimum version: 3 h flagship project, 1 h reading, 1 h documentation, 1 h relationships.

**Long-term objective:** Become a research-ready robotics engineer with enough demonstrated depth, research evidence, public artifacts, and trusted relationships to be competitive for strong graduate programs, research assistantships, and robotics/embodied-AI industry roles.

> The 24-week goal is not to “guarantee a publication” or connect directly with famous researchers. It is to build the evidence and relationships from which publications, recommendations, and opportunities realistically follow.

---

## 1. Starting-point assessment

You are not starting from zero. Your CV already contains unusually strong undergraduate material:

- **3.99/4.00 CGPA** with four Dean’s List semesters.
- **GRIP:** a deployed industrial computer-vision and parallel-SCARA rejection system, including inverse kinematics, trajectory control, pneumatics, BLDC actuation, and production constraints.
- **Mdrive:** an end-to-end BLDC motor-drive/FOC project involving PCB, power electronics, current sensing, STM32-class firmware, SVPWM, feedback control, and CAN.
- Robotics teaching, SLRC organization, ROS/ROS2, embedded systems, OpenCV, PyTorch, fabrication, and control.

Your real gap is **not a lack of engineering projects**. It is that the evidence currently does not tell a focused research story:

1. Little public, reproducible RL/embodied-AI work.
2. No clearly framed research question, benchmark, ablation, or paper-style report.
3. Projects need metrics, videos, diagrams, code, and explicit individual contributions.
4. Few research relationships and no visible open-source participation.
5. The CV has formatting/date problems and is too broad for a robotics-research target.

### Strategic positioning

Your strongest differentiator is:

> **A hardware-and-control engineer who can also conduct learning-based robotics experiments—not another student who has only trained models in notebooks.**

Build around the intersection of:

- learning-based control;
- robust/fault-tolerant robot behavior;
- sim-to-real and real-time constraints;
- embodied perception and action;
- low-cost, reproducible robotics.

---

## 2. The map

```text
FOUNDATIONS ───────► RESEARCH-GRADE FLAGSHIP ───────► PUBLIC EVIDENCE
RL + controls       robust sim-to-real control       code, tests, data,
robot learning      under faults/latency/noise       plots, report, video
       │                         │                           │
       └─────────────► OPEN SOURCE CONTRIBUTION ◄──────────┘
                                  │
                                  ▼
LOCAL MENTORS ─────► PEERS / PhD STUDENTS ─────► SENIOR RESEARCHERS
proposal feedback    technical conversations     only after proof of work
experiments          maintainers/collaborators    and a specific reason
                                  │
                                  ▼
                  PREPRINT / WORKSHOP / STUDENT VENUE
                                  │
                                  ▼
           GRAD SCHOOL + RESEARCH/ROBOTICS INDUSTRY OPTIONS
```

### Target profile by graduation

Aim to graduate with:

- 1 research-grade flagship project with rigorous evaluation;
- 2 supporting robotics artifacts (GRIP and Mdrive, professionally documented);
- 1 preprint/technical report and at least 1 credible submission, if results support it;
- 2–4 meaningful open-source contributions;
- 2 faculty/research mentors who know your work well enough to recommend you;
- 15–25 genuine research/industry relationships, rather than hundreds of shallow connections;
- a focused 1-page résumé, 2-page academic CV, project website, and research statement;
- evidence of fundamentals: controls, estimation, RL, robot learning, experiments, technical writing.

---

## 3. Flagship project

## Recommended topic

**Robust Sim-to-Real Control Under Actuator Faults, Observation Noise, and Latency**

### Core question

> Can curriculum-based domain randomization produce a learned controller that degrades more gracefully than standard RL and a classical controller when a robot experiences actuator weakness, sensor noise, communication delay, or model mismatch?

### Why this is the right project

- Connects RL directly to your control, BLDC/FOC, SCARA, and embedded strengths.
- Creates a meaningful bridge to Benjamin Swilling’s public focus on dynamic balance/fault-tolerant systems and Chris Bentzel’s simulation/RL/robot-software interests.
- Fits Chelsea Finn’s broad themes of generalization and learning through interaction.
- Can use open simulation and reproducible experiments without expensive robot hardware.
- Can later use GRIP/Mdrive for hardware-in-the-loop or limited sim-to-real validation.

### Minimum viable research scope

- **Environment:** MuJoCo + Gymnasium; begin with a standard manipulator or locomotion task. Model your parallel SCARA only after the experiment harness works.
- **Methods:** classical controller, PPO, SAC, and PPO/SAC with curriculum domain randomization. Do not add more algorithms unless the first comparison is complete.
- **Perturbations:** action latency, torque loss, encoder noise, payload/model mismatch.
- **Protocol:** at least 5 random seeds; held-out fault levels; identical evaluation episodes; confidence intervals; compute budget logged.
- **Metrics:** success rate, return, tracking error, time-to-completion, energy/control effort, worst-case performance, recovery after fault onset.
- **Ablations:** remove curriculum; remove one randomization family; train only at fixed fault severity.
- **Output:** tested repository, configuration files, reproducibility instructions, results CSVs, plots, 3–5 minute demo, project page, 6–8 page paper-style report.

### Scope ladder

- **Bronze:** rigorous simulation study with full reproducibility.
- **Silver:** hardware-in-the-loop validation using Mdrive telemetry/controller timing.
- **Gold:** limited real-system validation on the GRIP/SCARA setup, with safety constraints and permission to use the platform/data.

Bronze is enough for a strong portfolio. Never delay the complete simulation study while waiting for hardware.

### Week-4 fallback if compute or simulator complexity is too high

Switch to **resource-efficient robust navigation** rather than abandoning the research cycle: compare A*/Dijkstra, PPO or DQN, and optionally behavior cloning in MiniGrid first, then Webots/PyBullet if feasible. Study exactly one variable—unseen layouts, observation corruption, limited demonstrations, reward shaping versus curriculum, or a hybrid planner/RL controller. This CPU-first fallback preserves the same research standards while sharply reducing integration risk.

### Supporting project: open-source embodied-AI reproduction

Use **robosuite** first; use the much larger **RoboCasa** only if compute and setup permit. Reproduce one small published baseline or evaluate one controlled perturbation. Deliver one of:

- a documentation/test/bug-fix pull request;
- a reproducibility note with environment lockfile and exact commands;
- a small benchmark extension or evaluation script accepted by a maintainer.

Do not attempt to train a 7B VLA from scratch. OpenVLA itself reports large-scale pretraining on 64 A100 GPUs for 15 days. If studying a VLA, use inference, a small subset, parameter-efficient adaptation only if compute permits, or analyze released representations/results. The openpi README reports more than 8 GB GPU memory for inference, more than 22.5 GB for LoRA fine-tuning, and more than 70 GB for full fine-tuning, so confirm institutional/cloud compute before choosing it.

---

## 4. Weekly operating system

### Normal week: 12–15 hours

- 6–7 h flagship implementation/experiments
- 2–3 h RL/robot-learning fundamentals
- 2 h paper reading and research notes
- 1–2 h writing, repository, demo, or project page
- 1 h relationship building/open source

### Rules

1. Every week ends with a **visible artifact**: commit, plot, note, demo, issue, PR, or draft section.
2. Maintain `research-log.md`: hypothesis, change, result, interpretation, next action.
3. Do not report only the best seed.
4. Freeze evaluation before final experiments.
5. One flagship, one small reproduction, and professional documentation of existing work—no project sprawl.
6. Publish progress every two weeks, but never overclaim results.

---

## 5. The 24-week plan

| Week | Main work | Concrete exit criterion | Relationship/public action |
|---:|---|---|---|
| **1** | Audit GitHub/LinkedIn/CV; create roadmap board; reserve weekly time blocks; define compute/hardware access. | Public landing README, private tracker, baseline skills/compute inventory. | List 30 targets: 10 local, 10 PhD/early-career/maintainers, 5 peers, 5 senior people. |
| **2** | Refresh MDPs, value/policy methods, PPO/SAC; implement or cleanly reproduce small Gymnasium baselines. | Reproducible PPO/SAC runs, plots, environment lockfile, short learning note. | Follow relevant labs/maintainers; make two substantive comments based on actual papers/code. |
| **3** | Read 6 anchor papers: generalization/meta-RL, domain randomization, robust RL, sim-to-real, fault tolerance, chosen environment. Create literature matrix. | One-page problem statement plus matrix of method/data/metric/limitation/open question. | Meet one UoM faculty member/project supervisor; ask for 20 minutes of critique, not a position. |
| **4** | Write a 2-page proposal: question, hypotheses, methods, perturbations, metrics, compute budget, risks. Run one pilot. | Mentor-reviewed proposal and a go/no-go decision on environment/scope. | Contact a second local robotics/AI/control academic with the proposal attached. |
| **5** | Build environment wrapper and deterministic evaluation harness; add action latency and observation noise. | Unit tests; seeded rollouts; baseline environment video. | Open one well-researched issue only if you find a genuine reproducible problem. |
| **6** | Implement classical-control/reference baseline and logging pipeline. | Baseline controller evaluated across nominal and perturbed conditions. | Write a short technical note on the simulator/control assumptions. |
| **7** | Train nominal PPO and SAC using fixed budgets; diagnose stability. | Five-seed nominal baseline table; failures documented, not hidden. | Speak with one PhD student/maintainer working near the chosen tool or topic. |
| **8** | Build plotting/report pipeline; package v0.1. | Public milestone: setup instructions, first results, 60–90 second demo. | Progress post #1; ask for feedback on one specific technical decision. |
| **9** | Add fault injection: torque loss, stuck/biased actuator or payload/model mismatch. | Fault sweep across held-out severity levels. | Study Swilling/Bentzel public talks/posts; record three technical questions, send none yet unless artifact is relevant. |
| **10** | Implement curriculum/domain-randomized training. | Curriculum variant trained with matched compute budget. | Submit a small robosuite/Gymnasium/SB3 docs/test/bug PR if ready. |
| **11** | Run controlled ablations; compare nominal, randomization, and curriculum. | Preliminary ablation plots and written interpretation. | Mentor review #2; identify one realistic paper/workshop/student venue. |
| **12** | Midpoint replication and scope review. Cut weak extensions. | v0.2 release and 3-page midpoint report with limitations. | Send one value-first message to an accessible engineer/PhD student, linking the relevant result. |
| **13** | Freeze hypotheses, primary metrics, evaluation conditions, seed count, and exclusion rules. | Versioned evaluation protocol committed before final runs. | Progress post #2; share protocol and invite methodological criticism. |
| **14** | Final experiment batch A: main method comparisons. | Complete raw results with automatic provenance (config, commit, seed). | Offer a concise contribution to a local lab/student project where your control/embedded skill is useful. |
| **15** | Final experiment batch B: fault/severity generalization. | Held-out perturbation results and confidence intervals. | Talk to one researcher whose paper you reproduced; lead with what you found. |
| **16** | Failure taxonomy and robustness analysis; create rollout examples. | At least 3 recurring failure modes with quantitative frequency and videos. | If relevant, message Scott Nguyen with a calibration/inspection-specific artifact and one focused question. |
| **17** | Add only one high-value extension: HIL, GRIP/SCARA validation, or safety constraint. | Extension complete or explicitly dropped by the end of the week. | Mentor review #3; ask whether results are submission-worthy. |
| **18** | Independent rerun from a clean environment; documentation and tests. | Another person—or a clean machine—can reproduce one headline result. | Follow up with prior contacts by sharing the improved artifact, not “just checking in.” |
| **19** | Write paper: abstract, intro, related work, method, protocol. | Full skeleton with every figure/table placed and claims tied to evidence. | Ask 2 reviewers: one controls/robotics person and one ML person. |
| **20** | Write results, discussion, limitations, ethics/safety, reproducibility statement. | Complete draft v1; no placeholder results. | Progress post #3 focused on one honest insight or negative result. |
| **21** | Incorporate reviews; rerun only experiments necessary to resolve a real concern. | Draft v2 plus response-to-feedback log. | If a result directly relates, send a concise artifact-based note to a relevant senior target; otherwise wait. |
| **22** | Release code/data allowed for release, project page, demo, and technical report/preprint. | v1.0 repository, archived release/DOI if possible, 3–5 minute video, 6–8 page report. | Submit to a mentor-approved workshop/student/reproducibility venue if quality and timing fit. |
| **23** | Targeted outreach and applications packet. | Research résumé, academic CV, project one-pager, research statement paragraph, contact tracker. | Carefully contact 2–3 highly relevant people, each with a different, evidence-based reason. |
| **24** | Portfolio integration, mock interview, retrospective, next 6-month plan. | Final dashboard; mock research talk; applications/opportunity list; next milestone chosen. | Thank contributors/reviewers; send updates to people who gave useful feedback. |

---

## 6. Publication game plan

A peer-reviewed publication in 24 weeks is possible but not controllable. A **submission-quality manuscript** is controllable.

### Evidence ladder

1. Reproducible baseline.
2. Clear gap or failure mode.
3. One falsifiable hypothesis.
4. Controlled comparison under matched budgets.
5. Multiple seeds and held-out conditions.
6. Ablation and failure analysis.
7. External mentor review.
8. Technical report/preprint.
9. Workshop, undergraduate symposium, student forum, reproducibility track, or full venue only if the contribution fits.

### Authorship and mentoring

By Week 4, recruit a UoM academic mentor. Agree early on:

- expected contribution and meeting cadence;
- access/permission for GRIP data and hardware;
- publication target and authorship criteria;
- safety and intellectual-property restrictions;
- what can be released publicly.

### Avoid

- submitting to predatory pay-to-publish journals;
- claiming novelty before completing a literature search;
- turning a course project report into a “paper” without a research question;
- using factory data/code publicly without written permission;
- treating arXiv upload as peer-reviewed publication.

---

## 7. Relationship-building system

## The relationship ladder

```text
Observe → Understand → Reproduce → Contribute → Discuss → Collaborate → Ask
```

Do not jump from “followed on LinkedIn” to “please mentor/refer me.”

### Build a portfolio of relationships

| Tier | Target count | Who | What you offer/ask |
|---|---:|---|---|
| Local mentors | 5–8 | UoM robotics, control, AI, CV, embedded faculty/researchers | Proposal critique, monthly guidance, access, collaboration. |
| Near peers | 10–15 | MSc/PhD students and research engineers | Reproduction feedback, reading group, code review, joint experiment. |
| Maintainers | 5–10 | robosuite, RoboCasa, Gymnasium, SB3, MuJoCo ecosystem | Reproducible issues, tests, docs, small PRs. |
| Industry engineers | 5–10 | robotics software, controls, autonomy, inspection | Technical discussion, career calibration, artifact feedback. |
| Senior researchers/leads | 5 | Your scouted people | Contact only after a relevant artifact creates a real reason. |

### Weekly cadence

- 2 thoughtful public interactions with technical content;
- 1 new conversation with a peer, PhD student, maintainer, or local academic;
- 1 useful follow-up to an existing relationship;
- 1 progress post every two weeks;
- no more than 1 unsolicited senior-person message per week.

Track: person, work studied, overlap, value you can provide, last interaction, promised follow-up, next action. Never automate generic outreach.

At Moratuwa, begin with your existing project supervisors/references and the people around the **IntelliSense Lab**, **Artificial Intelligence Lab**, and Robotics/Control work. Prof. Buddhika Jayasekara is a particularly relevant public match for human-robot interaction, human-friendly robotics, machine learning, and intelligent systems—but approach based on a bounded proposal and fit, not name recognition alone.

---

## 8. The five scouted people

## Chelsea Finn — Stanford IRIS Lab / Physical Intelligence

**Verified public themes:** learning through robotic interaction at scale, broad robot intelligence, generalization, deep RL/meta-learning; co-author of OpenVLA; Stanford CS224R and CS330 materials are public.

**Study first:**

1. One CS224R lecture relevant to your method.
2. Meta-World/generalization work.
3. Current evaluation/reward work such as **RoboReward** and **PolaRiS**.
4. OpenVLA and the open ecosystems around **openpi, Octo, DROID, and SERL**, focusing on evaluation, data diagnostics, and adaptation—not full pretraining.
5. Current IRIS lab papers and the first-author students whose work is closest to yours.

**Meaningful path:** reproduce a small evaluation, contribute to an open artifact, write a rigorous note, discuss with a first author/PhD student, and only then send Chelsea a 100-word result/question. She is a long-term target, not your first cold contact.

**Respect the lab’s stated process:** IRIS explicitly asks prospective PhD applicants not to contact the lab directly about admission before being admitted. Outside-Stanford visitors are directed to the lab’s visiting-research form. Use those channels rather than trying to bypass them with a cold admissions email.

**Potential message trigger:** you have a clean result about robustness/generalization under action faults or latency and can state exactly how it complements or challenges an evaluation assumption.

## Yuke Zhu — UT Austin RPL / NVIDIA Research

**Verified public themes:** robotics and embodied AI, general-purpose robot autonomy, perception-action learning, cross-embodiment data, simulation, robot foundation models. Public ecosystems include robosuite, RoboCasa/RoboCasa365, Open X-Embodiment, and work around GR00T and sim/real data.

**Study first:**

1. RPL’s “Data Pyramid and Data Flywheel” research vision.
2. robosuite architecture and contribution guide.
3. RoboCasa paper, tasks, and evaluation design.
4. One current paper matching your scope, such as DreamGen, GR00T N1, MimicDroid, sim-and-real co-training, robust manipulation, or sim-to-real RL.
5. If compute is limited, use **AMAGO-2** or **Metamon** as lower-hardware RL reproduction entry points.

**Meaningful path:** make a useful robosuite/RoboCasa contribution or publish a small reproducibility/robustness benchmark. Contact the maintainer or first author first. Contact Yuke after your contribution has a stable URL and a precise connection to the lab’s agenda.

**Respect the lab’s stated process:** RPL says prospective graduate students should apply through UT Austin and mention the lab in the statement of purpose; no advance email is needed. Its published route for research interns/visitors is a form, with visits of six months or longer, and it asks people to contact the PI only for a specific question or research idea.

## Benjamin Swilling — Boston Dynamics, Spot robotics leadership

**Verified public themes:** long-term work on Spot and other Boston Dynamics platforms; dynamic balance; fault-tolerant systems; model-based and learning approaches in quadruped locomotion. His public profile describes work across Spot’s lifecycle, from locomotion algorithms to deployment quality.

**Study first:**

1. IFRR Quadruped Robotics panel.
2. Swilling’s public patent record on step-path selection, continuous slip recovery, gait fallback, and stair tracking.
3. Public Spot technical material on mobility, autonomy, safety, RL, and deployment.
4. Literature on actuator degradation and recovery in legged robots.

**Meaningful path:** your strongest bridge is the flagship’s fault-injection and graceful-degradation results, plus Mdrive/FOC expertise. Ask a narrow engineering question such as which simulated fault assumptions most often fail to reflect deployment reality. Do not ask for proprietary details.

## Chris Bentzel — Boston Dynamics, Atlas software leadership

**Verified public themes:** public profile identifies him with Atlas software; he has written about moving from games/software into robotics, the importance of 3D math, simulation, autonomy, RL, and interfaces. Public posts indicate a role leading software for the electric Atlas program.

**Study first:**

1. His article on game development and robotics.
2. Public electric-Atlas and RL demonstrations.
3. Simulation and developer tooling for robot behavior, observability, and debugging.

**Meaningful path:** build a polished simulation, failure replay/diagnostics tool, gamepad teleoperation interface, or concise note on making RL behavior inspectable. His own career transition makes a focused question about transferable software skills more appropriate than a generic job request. A particularly well-aligned question is: “For an RL behavior entering a production humanoid stack, which software interfaces and debugging guarantees matter most beyond reward and success rate?”

## Scott Nguyen — robotics software engineer, Gecko Robotics

**Verified:** Senior Robotics Software Engineer at Gecko Robotics, after work at Naval Nuclear Laboratory. His personal website links directly to the exact supplied LinkedIn handle, confirming that its material on robot calibration, inspection, pose estimation, ROS, controls, and 6/7-DOF systems belongs to the same Scott M. Nguyen. The personal résumé appears not yet updated for his recent move to Gecko.

**Study first:**

1. Gecko Robotics’ public inspection platforms and autonomy/software material.
2. His public posts/projects, especially calibration, inspection, perception, and reliability.
3. Compare his work themes with GRIP: production inspection, confidence handling, calibration, pose estimation, and system reliability.

**Meaningful path:** he is the most natural early contact because your GRIP project offers a concrete shared engineering context. Publish a GRIP case study with permission and metrics, then ask one question about calibration/reliability or the transition from university robotics to production robotics.

---

## 9. Message templates

### Connection request after studying a project

> Hi [Name]—I’m a third-year Electronic & Telecommunication Engineering student at the University of Moratuwa working on [specific project]. I studied your work on [specific item], especially [one precise insight]. I’m testing [one-sentence related experiment] and would value following your work here.

### After producing a relevant result

> Hi [Name]—your [paper/talk/project] shaped how I designed [specific part]. I reproduced/extended [specific element] under [fault/latency/domain-shift condition]. The main result was [one honest sentence], with code and plots here: [stable link]. I have one focused question: [question answerable in a few sentences]. No need for a call; even a quick pointer would help.

### Local faculty request

> Dear Dr. [Name], I’m developing a 24-week research project on robust learning-based robot control under actuator faults, latency, and model mismatch. My background includes a deployed vision-guided SCARA system and an in-progress BLDC/FOC drive. I’ve attached a two-page proposal with a bounded simulation-first scope. Could I get 20 minutes of critical feedback on the question and evaluation protocol? I’m specifically deciding [A vs B].

### Follow-up rule

One follow-up after 10–14 days, containing a new result or improvement. If there is no response, stop. Silence from a busy person is not a judgment of your potential.

---

## 10. Portfolio and CV rebuild

### Portfolio architecture

Your homepage should answer in 20 seconds:

1. What kind of engineer/researcher are you?
2. What have you built or discovered?
3. Where is the evidence?
4. How can someone contact you?

Use three featured cards:

1. **Robust RL flagship:** question, method, headline graph, video, paper, code.
2. **GRIP:** production problem, system diagram, your contribution, safety design, measured speed/accuracy/uptime, permitted video.
3. **Mdrive:** board render/photo, control architecture, current/velocity response plots, loop frequency, CAN integration, test results.

Every research repository needs: problem, install, exact reproduce command, expected output, data/license, tested versions, method diagram, results table with seeds, limitations, citation, and demo.

### Immediate CV corrections

The extracted CV shows several issues to fix now:

- Correct the **Education date alignment**: University of Moratuwa appears to have “June 2024–Present” displaced, while “2014–2022” appears beside the degree.
- Verify/remove “Colombo 10” if it is not the university location.
- Remove empty `[]` link placeholders and broken PDF characters.
- Replace the generic objective with a two-line research profile.
- Keep a **1-page industry résumé** and a **2-page academic CV**; the current version is roughly three pages.
- Remove the full references section and private phone numbers; use “References available on request” only if required.
- Put robotics/learning projects first; compress RF, networking, certifications, and school results.
- Quantify GRIP and Mdrive: accuracy/abstention rate, cycle time, trajectory error, line speed, loop frequency, current ripple, bandwidth, cost, team size, and your exact ownership—only with verified numbers.
- Add sections for Research Experience, Publications/Preprints, Open Source, and Selected Technical Writing as they become real.
- Make GitHub/LinkedIn/project URLs visible in plain text as well as clickable.

Suggested profile:

> Electronic and Telecommunication Engineering undergraduate (CGPA 3.99/4.00) focused on robot learning, robust control, and embodied AI. Built and deployed a vision-guided industrial rejection robot and currently develops an STM32-based BLDC/FOC drive; pursuing reproducible research in robust sim-to-real control.

---

## 11. Scoreboard

Review every Sunday.

| Dimension | Week 12 target | Week 24 target |
|---|---:|---:|
| Flagship | v0.2, baselines + preliminary ablations | v1.0, full evaluation + report + demo |
| Research writing | proposal + midpoint report | 6–8 page manuscript/preprint |
| Reproducibility | seeded scripts and configs | clean-machine reproduction + archived release |
| Existing projects | GRIP/Mdrive outlines | 2 polished case studies with verified metrics |
| Open source | 1 high-quality issue/PR | 2–4 useful contributions, at least 1 merged if possible |
| Relationships | 2 local mentors, 6 genuine conversations | 15–25 genuine contacts, 3–5 ongoing relationships |
| Public communication | 2–3 technical updates | 6–8 updates + project talk/video |
| Career package | corrected base CV | research résumé, academic CV, site, statement paragraph |

### Anti-metrics

Do not optimize for LinkedIn connection count, course certificates, GitHub commit count, number of half-finished repositories, paper count without venue quality, or messages sent.

---

## 12. After Week 24: graduation runway

Repeat the cycle at a higher level:

- **Next 6 months:** submit/revise the flagship; join a supervised project; complete real-system validation; obtain a substantial open-source contribution or research internship.
- **Following 6–12 months:** second project or extension with collaborators; present at a symposium/workshop; prepare English test and graduate-school materials if needed; identify 8–12 programs by advisor fit, not ranking alone.
- **Application period:** request letters from people who supervised actual work; tailor statements around a coherent research question; apply across ambitious, match, and safer options; apply to research assistant and robotics roles in parallel.

No plan makes it possible to “comfortably get any position.” The realistic aim is stronger: by graduation, make your evidence so clear that you have multiple credible pathways and can compete based on demonstrated ability rather than potential alone.

---

## 13. First 72 hours

1. Create the project board with all 24 weekly milestones.
2. Block 12–15 hours on the calendar for the next four weeks.
3. Create the flagship repository and `research-log.md`.
4. Correct the CV date/format errors and remove references/private numbers.
5. Send a meeting request to one UoM mentor with a one-paragraph project concept.
6. Read the RPL research vision and one CS224R lecture/paper relevant to robust RL.
7. Publish nothing to senior contacts yet; first earn a stable artifact worth sending.

---

## Sources used for the people/project map

- Chelsea Finn homepage and research/teaching links: https://ai.stanford.edu/~cbfinn/
- Stanford IRIS Lab: https://irislab.stanford.edu/
- OpenVLA project/code/model description: https://openvla.github.io/
- RoboReward: https://arxiv.org/abs/2601.00675
- PolaRiS: https://arxiv.org/abs/2512.16881
- Physical Intelligence openpi: https://github.com/Physical-Intelligence/openpi
- Octo: https://github.com/octo-models/octo
- DROID: https://github.com/droid-dataset/droid
- SERL: https://github.com/rail-berkeley/serl
- Yuke Zhu’s RPL Lab and research vision: https://rpl.cs.utexas.edu/
- RPL publications: https://rpl.cs.utexas.edu/publications/
- AMAGO-2: https://github.com/UT-Austin-RPL/amago
- Metamon: https://github.com/UT-Austin-RPL/metamon
- robosuite: https://robosuite.ai/
- RoboCasa/RoboCasa365: https://robocasa.ai/
- Open X-Embodiment: https://robotics-transformer-x.github.io/
- Benjamin Swilling bio and quadruped panel: http://ifrr.org/quadruped-robotics
- Benjamin Swilling patent index: https://patents.justia.com/inventor/benjamin-swilling
- Chris Bentzel on transferable game/software skills for robotics: https://www.inverse.com/innovation/boston-dynamics-chris-bentzel
- Boston Dynamics “Walk, Run, Crawl, RL Fun”: https://bostondynamics.com/video/walk-run-crawl-rl-fun/
- Scott Nguyen supplied LinkedIn profile: https://www.linkedin.com/in/scott-nguyen-103131192/
- Scott M. Nguyen’s personal résumé (links to the supplied LinkedIn handle): https://www.scottnguyen.blog/resume
- University of Moratuwa CSE research areas/labs: https://cse.mrt.ac.lk/research/areas-labs
- IRIS prospective-member contact policy: https://irislab.stanford.edu/contact.html
- RPL opportunities and application routes: https://rpl.cs.utexas.edu/opportunities/
- Prof. Buddhika Jayasekara, University of Moratuwa: https://uom.lk/staff/Jayasekara.AGBP
