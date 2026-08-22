# Start Here: First Reading Cycle

The bots found relevant evidence; they did **not** choose the project's novelty claim. This first cycle lets you compare established work before approving the question.

## Five anchor candidates

Read these in order over roughly two weeks:

1. **Robust Gymnasium (2025)** — inspect existing perturbation infrastructure before claiming a benchmark contribution.
2. **Nagabandi et al. (2019)** — direct hidden-dynamics adaptation under disabled joints and mid-rollout changes.
3. **UP-OSI (2017)** — explicit online system identification and a conditioned universal policy.
4. **DynaMITE-RL (2024)** — hidden temporal context changing within episodes; a major overlap check.
5. **RMA (2021)** — influential history-to-latent rapid motor adaptation with privileged training information.

Links and the secondary queue are in `queue.csv`. Create one note per paper using `paper-note-template.md`.

## Answer after each paper

1. What exactly is hidden from the controller?
2. Does the hidden variable stay fixed, switch once, drift, or recur?
3. What adapts online: recurrent state, inferred parameters, weights, model, or planner?
4. What privileged information is used in training or evaluation?
5. How is adaptation cost measured?
6. Which result directly affects our comparison?
7. What would our proposed study duplicate?
8. What remains uncertain after checking the primary source?

## Student decision meeting after five papers

We will not freeze the proposal until you can explain:

- generic robustness versus genuine adaptation;
- recurrent implicit memory versus explicit system identification;
- static context shifts versus within-episode fault processes;
- simple fault wrappers versus a diagnostic protocol;
- final return versus change-point-aligned recovery metrics.

Then choose among three candidate emphases—not conclusions:

1. **Fault identifiability:** when can different fault causes be distinguished from transitions?
2. **Held-out temporal fault grammar:** generalization to unseen schedules, compositions, and recovery events.
3. **Mechanism-matched adaptation bake-off:** robust, finite-memory, recurrent, explicit-ID, and oracle controllers under matched budgets.

Record your choice and reasoning in `research/decisions/decision-log.md`.
