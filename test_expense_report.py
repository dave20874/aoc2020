import pytest
from expense_report import ExpenseReport


def test_part1():
    cases = (("data/day1_example1.txt", 514579),
             ("data/day1_input.txt", 444019))

    for case in cases:
        (filename, expected) = case
        exp_rep = ExpenseReport(filename)
        assert exp_rep.part1() == expected

def test_part2():
    cases = (("data/day1_example1.txt", 241861950),
             ("data/day1_input.txt", 29212176)
            )

    for case in cases:
        (filename, expected) = case
        exp_rep = ExpenseReport(filename)
        assert exp_rep.part2() == expected

