import sys
from core import calc
import pytest


def test_add():
    assert calc.add(5, 10) == 15
    assert calc.add(-1, 1) == 0


@pytest.mark.skip()
def test_skip():
    assert calc.add(5, 10) == 15
    assert calc.add(-1, 1) == 0


@pytest.mark.skipif(sys.platform == "win32", reason="does not run on windows")
def test_skipif():
    assert calc.add(5, 10) == 15
    assert calc.add(-1, 1) == 0


@pytest.mark.xfail
def test_xfail():
    assert calc.add(5, 10) == 15
    assert calc.add(-1, 1) == 0


@pytest.mark.parametrize('num1, num2, result', [(7, 3, 10), (-1, 1, 0), (-1, 100, 99)])
def test_add2(num1, num2, result):
    assert calc.add(num1, num2) == result


def add_test():
    assert calc.add(5, 10) == 15
    assert calc.add(-1, 1) == 0


def test_add_2():
    assert calc.add(5, 10) == 15
    assert calc.add(-1, 1) == 0


