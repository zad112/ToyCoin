# ToyCoin

Toy blockchain for learning. Python 3, standard library only (pytest for tests). Build in small steps, commit after each.

## Goal

Target block time is ~30 seconds on an average CPU. Step 2 added proof-of-work: difficulty is leading zero bits (`DEFAULT_DIFFICULTY_BITS` in `toycoin/chain.py`); tune with `python -m toycoin.calibrate`. Tests must use low difficulty (e.g. 8 bits) to stay fast.

## Conventions

- Run tests with `python -m pytest`.
- Hashing must stay deterministic (sorted-key, compact JSON).
