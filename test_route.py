import pytest
from route import Route

def test_load():
    route = Route("data/day12_example1.txt")
    assert len(route.instructions) == 5

def test_part1():
    route = Route("data/day12_example1.txt")
    assert route.part1() == 25

def test_part2():
    route = Route("data/day12_example1.txt")
    assert route.part2() == 286
