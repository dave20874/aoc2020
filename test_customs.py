import pytest
from customs import Customs


def test_load():
    dummy = Customs("data/day6_example1.txt")
    assert len(dummy.groups) == 5


def test_reset():
    dummy = Customs("data/day6_example1.txt")
    dummy.reset()
    assert len(dummy.groups) == 0




def test_part1():
    dummy = Customs("data/day6_example1.txt")
    assert dummy.part1() == 11


def test_part2():
    dummy = Customs("data/day6_example1.txt")
    assert dummy.part2() == 6
