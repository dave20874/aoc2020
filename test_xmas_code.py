import pytest
from xmas_code import XmasCode

@pytest.fixture()
def ex1():
    return XmasCode("data/day9_example1.txt", 5)

def test_load(ex1):
    assert len(ex1.data) == 20
    assert ex1.data[10] == 102
    assert ex1.cursor == 0
    assert ex1.window_len == 5

def test_scan_preamble(ex1):
    ex1.scan_preamble()
    assert ex1.cursor == 5

def test_read_one(ex1):
    ex1.scan_preamble()
    check, value = ex1.read_one()
    assert check == True
    assert value == 40


def test_find_mismatch(ex1):
    ex1.scan_preamble()
    check, value = ex1.find_mismatch()
    assert check == False
    assert value == 127

def test_find_weakness(ex1):
    value = ex1.find_weakness()
    assert value == 62
