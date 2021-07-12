import pytest
from allergen_assessment import AllergenAssessment

def test_load():
    aa = AllergenAssessment("data/day21_example1.txt")
    assert len(aa.foods) == 4
    assert len(aa.foods[0][0]) == 4
    assert len(aa.foods[0][1]) == 2

def test_part1():
    aa = AllergenAssessment("data/day21_example1.txt")
    assert aa.part1() == 5

def test_part2():
        aa = AllergenAssessment("data/day21_example1.txt")
        assert aa.part2() == "mxmxvkd,sqjhc,fvjkl"