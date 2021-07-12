import pytest
from crab_combat import CrabCombat

def test_load():
    cc = CrabCombat("data/day22_example1.txt")
    assert len(cc.deck[1]) == 5
    assert len(cc.deck[2]) == 5
    assert cc.deck[1][0] == 9
    assert cc.deck[1][-1] == 1
    assert cc.deck[2][0] == 5
    assert cc.deck[2][-1] == 10
    assert cc.rounds == 0

def test_part1():
    cc = CrabCombat("data/day22_example1.txt")
    sum = cc.part1()
    assert sum == 306

def test_part2():
    cc = CrabCombat("data/day22_example1.txt")
    sum = cc.part2()
    assert sum == 291

