import pytest
from adapter_set import AdapterSet

def test_load1():
    a_set = AdapterSet("data/day10_example1.txt")
    assert len(a_set.adapters) == 13     # File has 11 entries and outlet and device add 2
    assert a_set.adapters[1] == 1        # Values are in the set in the right places.
    assert a_set.adapters[11] == 19

def test_load2():
    a_set = AdapterSet("data/day10_example2.txt")
    assert len(a_set.adapters) == 33    # File has 31 entries and outlet and device add 2

def test_part1_1():
    a_set = AdapterSet("data/day10_example1.txt")
    # Confirm that the analyzer solves part 1 of the example correctly.
    assert a_set.part1() == 35

def test_part1_2():
    a_set = AdapterSet("data/day10_example2.txt")
    # Confirm that the analyzer solves part 1 of the example correctly.
    assert a_set.part1() == 220

def test_part2():
    daily = AdapterSet("data/day10_example1.txt")
    # Confirm that the analyzer solves part 1 of the example correctly.
    assert daily.part2() == 8

def test_part2_2():
    daily = AdapterSet("data/day10_example2.txt")
    # Confirm that the analyzer solves part 2 of the example correctly.
    assert daily.part2() == 19208

