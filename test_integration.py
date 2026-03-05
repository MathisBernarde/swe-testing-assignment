from calculator import QuickCalc

def test_integration_full_user_flow():
    # Simulate user turning on calc, doing a math problem, and saving result
    calc = QuickCalc()
    result = calc.add(5, 3)
    calc.current_value = result
    assert calc.current_value == 8

def test_integration_clear_after_calculation():
    # Simulate user doing math, then pressing clear
    calc = QuickCalc()
    calc.current_value = calc.multiply(10, 5)
    calc.clear()
    assert calc.current_value == 0.0