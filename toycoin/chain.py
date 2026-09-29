from toycoin.block import Block

GENESIS_PREVIOUS_HASH = "0" * 64


class Blockchain:
    def __init__(self):
        self.chain = [self._create_genesis_block()]

    @staticmethod
    def _create_genesis_block():
        # Fixed timestamp so every node builds an identical genesis block.
        return Block(0, "genesis", GENESIS_PREVIOUS_HASH, timestamp=0)

    @property
    def last_block(self):
        return self.chain[-1]

    def add_block(self, data):
        block = Block(len(self.chain), data, self.last_block.hash)
        self.chain.append(block)
        return block

    def is_valid(self):
        """Check every block's stored hash and its link to the previous block."""
        if self.chain[0].hash != self.chain[0].compute_hash():
            return False
        for prev, cur in zip(self.chain, self.chain[1:]):
            if cur.hash != cur.compute_hash():
                return False
            if cur.previous_hash != prev.hash:
                return False
        return True
