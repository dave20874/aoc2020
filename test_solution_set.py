import pytest
from solution_set import SolutionSet

@pytest.fixture()
def soln_set():
    return SolutionSet()

def test_get_solution(soln_set):
    assert soln_set.get_solution(0, 1) == 90909
    assert soln_set.get_solution(0, 2) == 55902
    assert soln_set.get_solution(99, 1) is None
    assert soln_set.get_solution(0, 3) is None


def test_get_num_solutions(soln_set):
    assert soln_set.get_num_solutions() > 0

