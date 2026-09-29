# ToyCoin

Toy blockchain for learning. Python 3, standard library only (pytest for tests). Build in small steps, commit after each.

## Goal

Target block time is ~30 seconds on an average CPU. Proof-of-work and difficulty tuning are added in step 2 (not yet implemented).

## Conventions

- Run tests with `python -m pytest`.
- Hashing must stay deterministic (sorted-key, compact JSON).
