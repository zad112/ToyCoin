# ToyCoin

A toy blockchain for learning. Python 3, standard library only (pytest for tests).

## Layout

- `toycoin/block.py` — `Block` with SHA-256 `compute_hash()` over deterministic JSON, plus `mine()`.
- `toycoin/chain.py` — `Blockchain` with a genesis block, `add_block()` (mines) and `is_valid()` (hashes, links, proof-of-work).
- `toycoin/calibrate.py` — measures your hash rate and suggests difficulty bits for ~30s blocks (`python -m toycoin.calibrate`).
- `tests/test_chain.py` — pytest tests, including tamper detection.

## Run tests

    python -m pytest

## Roadmap

1. Blocks and chain with hash-link validation (done).
2. Proof-of-work mining (done): difficulty is the number of leading zero bits, default 22. Block times are random (mining is a lottery), so ~30s is an average; each extra bit doubles it. Run the calibrate script to tune for your CPU.
3. Ideas: automatic difficulty retargeting, transactions, a faster mining loop.
