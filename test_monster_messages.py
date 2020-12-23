from monster_messages import MonsterMessages
import pytest

def test_load():
    mm = MonsterMessages("data/day19_example1.txt")
    assert len(mm.rules) == 6
    assert len(mm.messages) == 5

def test_gen_re():
    mm = MonsterMessages("data/day19_example1.txt")
    s = mm.rules[0].form_re(mm.rules)
    assert s == "a(?:(?:aa|bb)(?:ab|ba)|(?:ab|ba)(?:aa|bb))b"

def test_matching():
    mm = MonsterMessages("data/day19_example1.txt")
    assert mm.num_match() == 2

def test_matching_example2():
    mm = MonsterMessages("data/day19_example2.txt")
    assert mm.num_match() == 3

def test_part2():
    mm = MonsterMessages("data/day19_example2.txt")
    assert mm.part2() == 12
