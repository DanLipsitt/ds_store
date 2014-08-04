from mock import Mock
from ds_store.buddy import Block

def test_read_two_unsigned_ints():
    allocator = Mock(**{'read.return_value': b'\x00\x00\x00\x01\x00\x00\x00\x00'})
    block = Block(allocator, 0, 8)
    assert block.read('>II') == (1, 0)
