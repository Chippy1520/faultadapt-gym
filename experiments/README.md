# Experiment Organization

Store only versioned configurations and small metadata in Git. Raw runs belong under ignored `runs/`.

Every final run must record:

- configuration name;
- git commit;
- environment and fault profile;
- method and hyperparameters;
- seed;
- start/end time and hardware;
- raw artifact location;
- exit status.

Recommended ID: `<date>-<env>-<method>-<fault>-s<seed>`.
