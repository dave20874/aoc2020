import pytest
from jurassic_jigsaw import JurassicJigsaw

def test_load():
    jj = JurassicJigsaw("data/day20_example1.txt", 3, 3)
    assert len(jj.tiles) == 9

    jj = JurassicJigsaw("data/day20_input.txt", 12, 12)
    assert len(jj.tiles) == 144

def test_part1():
    jj = JurassicJigsaw("data/day20_example1.txt", 3, 3)
    assert jj.part1() == 20899048083289

def test_part2():
    jj = JurassicJigsaw("data/day20_example1.txt", 3, 3)
    assert jj.part2() == 273
