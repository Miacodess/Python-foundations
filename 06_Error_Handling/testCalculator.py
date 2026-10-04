import pytest
from SafeCalculator import InvalidOperatorError, Calc


def testAddition():
    assert Calc(2, 3, "+") == 5


def testDivision():
    assert Calc(10, 4, "/") == 2.5


def testRemainderAndPower():
    assert Calc(10, 3, "%") == 1
    assert Calc(2, 3, "**") == 8


def testDivisionByZeroRaises():
    with pytest.raises(ZeroDivisionError):
        Calc(5, 0, "/")


def testRemainderByZeroRaises():
    with pytest.raises(ZeroDivisionError):
        Calc(5, 0, "%")


def testInvalidOperatorRaises():
    with pytest.raises(InvalidOperatorError):
        Calc(5, 2, "x")
