# ToyCoin

A toy blockchain for learning. Python 3, standard library only (pytest for tests).

## Layout

- `toycoin/block.py` — `Block` with SHA-256 `compute_hash()` over deterministic JSON.
- `toycoin/chain.py` — `Blockchain` with a genesis block, `add_block()` and `is_valid()`.
- `tests/test_chain.py` — pytest tests, including tamper detection.

## Run tests

    python -m pytest

## Roadmap

1. Blocks and chain with hash-link validation (done).
2. Proof-of-work mining, tuned for ~30 second blocks on an average CPU.
