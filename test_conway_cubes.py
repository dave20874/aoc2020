from conway_cubes import ConwayCubes
import pytest


def test_load():
    cc = ConwayCubes("data/day17_example1.txt", 3)
    assert len(cc.initial) == 5
    assert cc.active_cubes() == 5
    assert (0, 0) not in cc.initial
    assert cc.initial[(1, 0)] == True
    assert (2, 0) not in cc.initial
    assert (0, 1) not in cc.initial
    assert (1, 1) not in cc.initial
    assert cc.initial[(2, 1)] == True
    assert cc.initial[(0, 2)] == True
    assert cc.initial[(1, 2)] == True
    assert cc.initial[(2, 2)] == True


def test_step():
    cc = ConwayCubes("data/day17_example1.txt", 3)
    cc.step()
    assert cc.active_cubes() == 11;
    cc.step()
    assert cc.active_cubes() == 21;
    cc.step()
    assert cc.active_cubes() == 38;
    cc.step()
    cc.step()
    cc.step()
    assert cc.active_cubes() == 112;

def test_part2():
    cc = ConwayCubes("data/day17_example1.txt", 4)
    cc.step()
    cc.step()
    cc.step()
    cc.step()
    cc.step()
    cc.step()
    assert cc.active_cubes() == 848;
