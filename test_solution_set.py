import pytest
from solution_set import SolutionSet

@pytest.fixture()
def soln_set():
    return SolutionSet()

def test_get_solution(soln_set):
    # Confirm test entries were read successfully
    assert soln_set.get_solution(0, 1) == 90909
    assert soln_set.get_solution(0, 2) == 55902

    # Invalid days have no solution
    assert soln_set.get_solution(99, 1) is None

    # Invalid parts have no solution
    assert soln_set.get_solution(0, 3) is None


def test_get_num_solutions(soln_set):
    # Increment number as we open up new days of the challenge.
    assert soln_set.get_num_solutions() == 3

