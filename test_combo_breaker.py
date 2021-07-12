from combo_breaker import ComboBreaker

def test_load():
    cb = ComboBreaker("data/day25_example1.txt")
    assert cb.pubkey1 == 5764801
    assert cb.pubkey2 == 17807724

def test_get_loop_size():
    cb = ComboBreaker("data/day25_example1.txt")
    n, size = cb.get_smaller_loop_size()
    assert n == 1
    assert size == 8

def test_get_session_key():
    cb = ComboBreaker("data/day25_example1.txt")
    n, size = cb.get_smaller_loop_size()
    key = cb.get_session_key(n, size)
    assert key == 14897079