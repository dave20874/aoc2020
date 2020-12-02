import pytest
from password_db import PasswordDb

@pytest.fixture()
def db():
    return PasswordDb()

def test_load_file(db):
    cases = (("data/day2_example.txt", 3),
             ("data/day2_input.txt", 1000))
    for case in cases:
        (filename, expected) = case
        db.load_file(filename)
        assert db.num_records() == expected


def test_num_valid(db):
    cases = (("data/day2_example.txt", 2),)
    for case in cases:
        (filename, expected_valid) = case
        db.load_file(filename)
        assert db.num_valid() == expected_valid

def test_num_valid2(db):
    cases = (("data/day2_example.txt", 1),)
    for case in cases:
        (filename, expected_valid) = case
        db.load_file(filename)
        assert db.num_valid2() == expected_valid
