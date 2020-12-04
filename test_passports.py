import pytest
from passports import Passports


def test_load_file():
    passports = Passports("data/day4_example1.txt")
    assert len(passports.records) == 4

    fields_per_rec = ((0, 8), (1, 7), (2, 7), (3, 6))
    for rec_no, num_fields in fields_per_rec:
        assert len(passports.records[rec_no]) == num_fields

def test_num_valid():
    passports = Passports("data/day4_example1.txt")
    assert passports.validate() == 2

    which_valid = ((0, True), (1, False), (2, True), (3, False))
    for rec_no, expected in which_valid:
        assert passports.is_valid(passports.records[rec_no]) == expected

def test_valid_fields():
    passports = Passports("data/day4_example2.txt")
    assert len(passports.records) == 8
    assert passports.validate(check_fields=True) == 4

    assert passports.invalid["eyr"] == 3
    assert passports.invalid["hgt"] == 2
    assert passports.invalid["pid"] == 2
    assert passports.invalid["hcl"] == 2
    assert passports.invalid["byr"] == 1
    assert passports.invalid["iyr"] == 1
    assert passports.invalid["ecl"] == 1



