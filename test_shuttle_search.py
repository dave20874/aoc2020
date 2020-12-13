import pytest
from shuttle_search import Schedule

def test_load():
    schedule = Schedule("data/day13_example1.txt")
    assert len(schedule.buses) == 8
    assert schedule.time == 939

def test_part1():
    schedule = Schedule("data/day13_example1.txt")
    assert schedule.part1() == 295

def test_part2():
    cases = (("data/day13_example1.txt", 1068781),
             ("data/day13_example2.txt", 3417),
             ("data/day13_example3.txt", 754018),
             ("data/day13_example4.txt", 779210),
             ("data/day13_example5.txt", 1261476),
             ("data/day13_example6.txt", 1202161486),
             )

    for filename, expected in cases:
        schedule = Schedule(filename)
        assert schedule.part2() == expected

