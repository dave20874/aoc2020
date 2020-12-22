from operator_order import OperatorOrder
import pytest

def test_load():
    oo = OperatorOrder("data/day18_example1.txt")
    assert len(oo.expressions) == 5

def test_eval1():
    oo = OperatorOrder("data/day18_example1.txt")
    assert oo.expressions[0].eval1() == 71
    assert oo.expressions[1].eval1() == 26
    assert oo.expressions[2].eval1() == 437
    assert oo.expressions[3].eval1() == 12240
    assert oo.expressions[4].eval1() == 13632

def test_eval2():
    oo = OperatorOrder("data/day18_example2.txt")
    assert oo.expressions[0].eval2() == 51
    assert oo.expressions[1].eval2() == 46
    assert oo.expressions[2].eval2() == 1445
    assert oo.expressions[3].eval2() == 669060
    assert oo.expressions[4].eval2() == 23340

def test_part1():
    oo = OperatorOrder("data/day18_example1.txt")
    assert oo.part1() == 71+26+437+12240+13632

def test_part2():
    oo = OperatorOrder("data/day18_example2.txt")
    assert oo.part2() == 51 + 46 + 1445 + 669060 + 23340
