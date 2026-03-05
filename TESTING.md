# Testing Strategy for Quick-Calc

## Strategy Overview
My testing strategy focuses on ensuring functional correctness and preventing regressions. I tested all functional requirements (addition, subtraction, multiplication, division, clear) and critical edge cases (division by zero, negative numbers). I did not test non-functional attributes like performance or scalability, as this is a simple local application.

## Lecture Concepts Applied

1. **The Testing Pyramid:** My test suite reflects the pyramid by having a larger base of isolated Unit Tests (8 tests) that check the core logic, and a smaller number of Integration Tests (2 tests) that verify how the application handles state changes and user workflows.
2. **Black-box vs White-box Testing:** The unit tests were written using a white-box approach, as I knew the internal structure of the `calculator.py` module. [cite_start]The integration tests simulate black-box testing by testing inputs and outputs just as a user would interact with the system[cite: 233, 234].
3. [cite_start]**Functional vs Non-Functional Testing:** I exclusively performed Functional Testing to verify that the software meets specific requirements[cite: 220, 221]. [cite_start]I intentionally skipped non-functional testing (like checking how the app behaves under stress with multiple users [cite: 251, 252]) since it is a single-user offline tool.
4. **Regression Testing:** By using an automated test runner (`pytest`), this suite acts as a regression test suite. [cite_start]If I change the code in the future, running the suite confirms the changes don't break the application[cite: 260].

## Test Results Summary

| Test Name | Type | Status |
| :--- | :--- | :--- |
| `test_add` | Unit | PASS |
| `test_subtract` | Unit | PASS |
| `test_multiply` | Unit | PASS |
| `test_divide` | Unit | PASS |
| `test_divide_by_zero` | Unit | PASS |
| `test_add_negative_numbers` | Unit | PASS |
| `test_multiply_large_numbers` | Unit | PASS |
| `test_clear_function` | Unit | PASS |
| `test_integration_full_user_flow` | Integration | PASS |
| `test_integration_clear_after_calculation` | Integration | PASS |