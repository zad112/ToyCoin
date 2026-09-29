import hashlib
import json
import time


def meets_difficulty(hash_hex, difficulty_bits):
    """True if the hash, read as a 256-bit number, has >= difficulty_bits leading zero bits."""
    return int(hash_hex, 16) >> (256 - difficulty_bits) == 0


class Block:
    def __init__(self, index, data, previous_hash, timestamp=None, nonce=0):
        self.index = index
        self.timestamp = time.time() if timestamp is None else timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = nonce
        self.hash = self.compute_hash()

    def mine(self, difficulty_bits):
        """Increment nonce until the hash has `difficulty_bits` leading zero bits."""
        while not meets_difficulty(self.hash, difficulty_bits):
            self.nonce += 1
            self.hash = self.compute_hash()
        return self.hash

    def compute_hash(self):
        """SHA-256 over a deterministic JSON serialization of the block's fields."""
        payload = json.dumps(
            {
                "index": self.index,
                "timestamp": self.timestamp,
                "data": self.data,
                "previous_hash": self.previous_hash,
                "nonce": self.nonce,
            },
            sort_keys=True,
            separators=(",", ":"),
        )
        return hashlib.sha256(payload.encode("utf-8")).hexdigest()
