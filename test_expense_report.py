import pytest
from expense_report import ExpenseReport


def test_part1():
    cases = (("data/day1_example1.txt", 514579),)

    for case in cases:
        (filename, expected) = case
        exp_rep = ExpenseReport(filename)
        assert exp_rep.part1() == expected

def test_part2():
    cases = (("data/day1_example1.txt", 241861950),)

    for case in cases:
        (filename, expected) = case
        exp_rep = ExpenseReport(filename)
        assert exp_rep.part2() == expected

