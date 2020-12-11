import pytest
from seating import Seating

def test_load():
    seating = Seating("data/day11_example1.txt")
    assert seating.max_x == 9
    assert seating.max_y == 9
    assert (1, 0) not in seating.is_seat
    assert (0, 1) in seating.is_seat
    assert seating.num_occupied() == 0

def test_step():
    seating = Seating("data/day11_example1.txt")
    seating.comp_neighbors()
    stable = seating.step()
    assert not stable
    assert seating.num_occupied() == len(seating.is_seat)

def test_part1():
    seating = Seating("data/day11_example1.txt")

    # Verify that the example problem gives the example solution
    assert seating.part1() == 37


def test_part2():
    seating = Seating("data/day11_example1.txt")

    # Verify that the example problem gives the example solution
    assert seating.part2() == 26
