import pytest

from series import fibonacci


def test_fibonacci_0():
    actual = fibonacci(0)
    expected = 0
    assert actual == expected
