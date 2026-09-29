"""Measure this CPU's hash rate and suggest difficulty bits for the target block time."""
import math
import time

from toycoin.block import Block
from toycoin.chain import TARGET_BLOCK_TIME


def main(samples=200_000):
    block = Block(1, "calibrate", "0" * 64)
    start = time.perf_counter()
    for nonce in range(samples):
        block.nonce = nonce
        block.compute_hash()
    rate = samples / (time.perf_counter() - start)
    bits = math.log2(rate * TARGET_BLOCK_TIME)
    print(f"{rate:,.0f} hashes/s")
    print(f"difficulty for ~{TARGET_BLOCK_TIME}s blocks: {bits:.2f} bits (use {round(bits)})")


if __name__ == "__main__":
    main()
