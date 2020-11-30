import pytest
from aoc2020 import Day1

@pytest.fixture()
def day1():
    return Day1()

def test_d1p1(day1):
    assert day1.part1() == 0

def test_d1p2(day1):
    assert day1.part2() == 0
