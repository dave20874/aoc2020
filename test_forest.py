import pytest
from functools import reduce
from forest import Forest

@pytest.fixture()
def forest():
    return Forest("data/day3_example1.txt")

def test_load(forest):
    assert forest.height == 11
    assert forest.width == 11
    assert (2, 0) in forest.tree_at
    assert (2, 1) not in forest.tree_at

def test_is_tree(forest):
    assert forest.is_tree(2, 0)
    assert not forest.is_tree(2, 1)

def test_get_num_trees(forest):
    assert forest.get_num_trees(3, 1) == 7

def test_multi_slope(forest):
    slopes = ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2))

    trees_hit = map((lambda slope: forest.get_num_trees(slope[0], slope[1])), slopes)
    prod = reduce((lambda x, y: x * y), trees_hit)
    assert prod == 336


