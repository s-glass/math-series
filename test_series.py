import pytest

from series import fibonacci
from series import lucas
from series import sum_series

def test_fibonacci_0():
    actual = fibonacci(0)
    expected = 0
    assert actual == expected


def test_lucas_0():
    actual = lucas(0)
    expected = 2
    assert actual == expected


def test_sum_series_fib_0():
    actual = sum_series(7,0,1)
    expected = 13
    assert actual == expected


def test_sum_series_lucas_0():
    actual = sum_series(7,2,1)
    expected = 29
    assert actual == expected