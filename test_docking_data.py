import pytest
from docking_data import DockingData

def test_reset():
    dd = DockingData()
    dd.load("data/day14_example1.txt")
    dd.reset()

    assert len(dd.mem) == 0
    assert dd.and_mask == 0
    assert dd.or_mask == 0

def test_load():
    dd = DockingData()
    dd.load("data/day14_example1.txt")

    assert dd.or_mask == 64
    assert dd.and_mask == 0xFFFFFFFFD

def test_part1():
    dd = DockingData()
    dd.load("data/day14_example1.txt")

    assert dd.get_sum() == 165

def test_part2():
    dd = DockingData()
    dd.load2("data/day14_example2.txt")

    # assert True
    assert dd.get_sum() == 208
