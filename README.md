# Quick-Calc

Quick-Calc is a lightweight, reliable calculator application built in Python. It supports basic arithmetic operations including addition, subtraction, multiplication, and division, along with a robust clear function and division by zero handling.

## Setup Instructions
1. Ensure you have Python 3 installed on your machine.
2. Clone this repository.
3. Install the testing dependency by running: `pip install -r requirements.txt`

## How to Run Tests
To execute the entire test suite (unit and integration tests), run the following command in the root directory:
`pytest`

## Testing Framework Research
For this project, I considered **Pytest** and **Unittest**. 

**Unittest** is built into the Python standard library, which means no external dependencies are required. However, it requires a lot of boilerplate code (creating classes that inherit from `unittest.TestCase`) and its assertion syntax (like `assertEqual`) can feel non-pythonic.

**Pytest**, on the other hand, allows developers to write simple, compact test functions without classes. It uses the standard Python `assert` keyword, making tests much easier to read and write. I chose **Pytest** for Quick-Calc because its simplicity speeds up development and its detailed failure outputs make debugging much easier.