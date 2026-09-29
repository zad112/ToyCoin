from toycoin.chain import Blockchain


def make_chain(n=3):
    bc = Blockchain(difficulty_bits=8)
    for i in range(n):
        bc.add_block(f"tx {i}")
    return bc


def test_genesis():
    bc = Blockchain()
    assert len(bc.chain) == 1
    assert bc.chain[0].index == 0
    assert bc.is_valid()


def test_add_block_links_and_validates():
    bc = make_chain()
    assert len(bc.chain) == 4
    for prev, cur in zip(bc.chain, bc.chain[1:]):
        assert cur.previous_hash == prev.hash
    assert bc.is_valid()


def test_hash_is_deterministic():
    bc = make_chain(1)
    block = bc.chain[1]
    assert block.compute_hash() == block.compute_hash() == block.hash


def test_tampering_data_invalidates_chain():
    bc = make_chain()
    bc.chain[1].data = "evil"
    assert not bc.is_valid()


def test_tampering_and_rehashing_breaks_link():
    bc = make_chain()
    bc.chain[1].data = "evil"
    bc.chain[1].hash = bc.chain[1].compute_hash()  # attacker fixes the block's own hash
    assert not bc.is_valid()  # but the next block's previous_hash no longer matches


def test_mined_blocks_meet_difficulty():
    bc = make_chain()
    for block in bc.chain[1:]:
        assert int(block.hash, 16) >> (256 - bc.difficulty_bits) == 0


def test_block_without_proof_of_work_is_invalid():
    bc = make_chain(1)
    block = bc.chain[1]
    # Find a nonce that does NOT satisfy the difficulty, with a consistent hash.
    while int(block.hash, 16) >> (256 - bc.difficulty_bits) == 0:
        block.nonce += 1
        block.hash = block.compute_hash()
    assert not bc.is_valid()
