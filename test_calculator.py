import pytest
from calculator import QuickCalc

def test_add():
    calc = QuickCalc()
    assert calc.add(5, 3) == 8

def test_subtract():
    calc = QuickCalc()
    assert calc.subtract(10, 4) == 6

def test_multiply():
    calc = QuickCalc()
    assert calc.multiply(6, 7) == 42

def test_divide():
    calc = QuickCalc()
    assert calc.divide(10, 2) == 5

def test_divide_by_zero():
    calc = QuickCalc()
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calc.divide(5, 0)

def test_add_negative_numbers():
    calc = QuickCalc()
    assert calc.add(-5, -10) == -15

def test_multiply_large_numbers():
    calc = QuickCalc()
    assert calc.multiply(1000000, 1000000) == 1000000000000

def test_clear_function():
    calc = QuickCalc()
    calc.current_value = 50
    assert calc.clear() == 0.0

def test_add_floats():
    calc = QuickCalc()
    assert calc.add(0.1, 0.2) == pytest.approx(0.3)

def test_invalid_types():
    calc = QuickCalc()
    with pytest.raises(TypeError):
        calc.add("10", 5)