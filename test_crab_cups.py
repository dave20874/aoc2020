import pytest
from crab_cups import CrabCups

def test_part1():
    cc = CrabCups("389125467")
    assert cc.part1(100) == 67384529

def test_part2():
    cc = CrabCups("389125467", 1000000)
    assert cc.part2(10000000) == 149245887792
