import pytest

from bag_rules import BagRules

def test_bag_rules():
    rules = BagRules("data/day7_example1.txt")
    assert rules.num_rules() == 9

def test_num_outer():
    rules = BagRules("data/day7_example1.txt")
    assert rules.num_outer("shiny gold") == 4

def test_contained_in():
    rules = BagRules("data/day7_example2.txt")
    assert rules.contained_in("shiny gold") == 126
