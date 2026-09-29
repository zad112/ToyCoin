from toycoin.block import Block, meets_difficulty

GENESIS_PREVIOUS_HASH = "0" * 64

# Each extra bit doubles the expected work. Pure-Python SHA-256 mining runs at
# roughly 200k hashes/s on one core, so 22 bits (~4.2M hashes) is ~20s and
# 23 bits is ~40s. Run `python -m toycoin.calibrate` to pick a value for your CPU.
DEFAULT_DIFFICULTY_BITS = 22
TARGET_BLOCK_TIME = 30  # seconds


class Blockchain:
    def __init__(self, difficulty_bits=DEFAULT_DIFFICULTY_BITS):
        self.difficulty_bits = difficulty_bits
        self.chain = [self._create_genesis_block()]

    @staticmethod
    def _create_genesis_block():
        # Fixed timestamp so every node builds an identical genesis block.
        # The genesis block is exempt from proof-of-work.
        return Block(0, "genesis", GENESIS_PREVIOUS_HASH, timestamp=0)

    @property
    def last_block(self):
        return self.chain[-1]

    def add_block(self, data):
        """Mine a new block on top of the chain and append it."""
        block = Block(len(self.chain), data, self.last_block.hash)
        block.mine(self.difficulty_bits)
        self.chain.append(block)
        return block

    def is_valid(self):
        """Check hashes, hash links and proof-of-work for every block."""
        if self.chain[0].hash != self.chain[0].compute_hash():
            return False
        for prev, cur in zip(self.chain, self.chain[1:]):
            if cur.hash != cur.compute_hash():
                return False
            if cur.previous_hash != prev.hash:
                return False
            if not meets_difficulty(cur.hash, self.difficulty_bits):
                return False
        return True
