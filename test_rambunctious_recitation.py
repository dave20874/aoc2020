import pytest
from rambunctious_recitation import Recitation

def test_load():
    rec = Recitation("data/day15_example1.txt")
    assert len(rec.start_seq) == 3
    assert len(rec.last_spoken) == 0

def test_part1():
    cases = (("data/day15_example1.txt", 436),
             ("data/day15_example2.txt", 1),
             ("data/day15_example3.txt", 10),
             ("data/day15_example4.txt", 27),
             ("data/day15_example5.txt", 78),
             ("data/day15_example6.txt", 438),
             ("data/day15_example7.txt", 1836),
             )

    for filename, expected in cases:
        rec = Recitation(filename)
        rec.start()
        assert rec.play_to(2020) == expected

"""  Takes too long!
def test_part2():
    cases = (("data/day15_example1.txt", 175594),
             ("data/day15_example2.txt", 2578),
             ("data/day15_example3.txt", 3544142),
             ("data/day15_example4.txt", 261214),
             ("data/day15_example5.txt", 6895259),
             ("data/day15_example6.txt", 18),
             ("data/day15_example7.txt", 362),
             )

    for filename, expected in cases:
        rec = Recitation(filename)
        rec.start()
        assert rec.play_to(30000000) == expected
"""
