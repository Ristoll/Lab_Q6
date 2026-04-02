from setup import add, divide, mod, multiply, power, subtract
import pytest

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(0, 10) == 0

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(0, 0) == 0
    assert subtract(-1, -1) == 0

def test_divide():
    assert divide(6, 3) == 2
    assert divide(-6, 3) == -2
    with pytest.raises(ValueError):
        divide(5, 0)

def test_power():
    assert power(2, 3) == 8
    assert power(5, 0) == 1
    assert power(0, 5) == 0

def test_mod():
    assert mod(5, 3) == 2
    assert mod(10, 2) == 0
    assert mod(7, 7) == 0