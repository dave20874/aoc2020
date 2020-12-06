import pytest
from aoc2020 import *
from solution_set import SolutionSet

# ---------------------------------------------------------------
# Test fixtures return daily puzzle solvers to be tested
@pytest.fixture()
def days(scope='module'):
    day_list = (None, Day1(), Day2(), Day3(), Day4(), Day5(), Day6(), Day7(), Day8(), Day9(), Day10(),
            Day11(), Day12(), Day13(), Day14(), Day15(), Day16(), Day17(), Day18(), Day19(), Day20(),
            Day21(), Day22(), Day23(), Day24(), Day25())

    return day_list

@pytest.fixture(scope='module')
def solns():
    return SolutionSet()

# ---------------------------------------------------------------
# Test cases, one for each part of each day.

def test_part1(days, solns):
    for d in range(25):
        day = d+1
        if days[day].part1() is not None:
            assert days[day].part1() == solns.get_solution(day, 1)

def test_part2(days, solns):
    for d in range(25):
        day = d + 1
        if days[day].part2() is not None:
            assert days[day].part2() == solns.get_solution(day, 2)



