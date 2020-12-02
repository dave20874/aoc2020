import pytest
from aoc2020 import *

@pytest.fixture()
def day1():
    return Day1()

@pytest.fixture()
def day2():
    return Day2()

def test_d1p1(day1):
    assert day1.part1() == 444019

def test_d1p2(day1):
    assert day1.part2() == 29212176

def test_d2p1(day2):
    assert day2.part1() == 625

def test_d2p2(day2):
    assert day2.part2() == 391


