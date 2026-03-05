from typing import Union

Number = Union[int, float]

class QuickCalc:
    """A simple calculator application."""

    def __init__(self) -> None:
        """Initialize the calculator with a current value of 0.0."""
        self.current_value: Number = 0.0

    def add(self, a: Number, b: Number) -> Number:
        """Add two numbers and store the result."""
        self.current_value = a + b
        return self.current_value

    def subtract(self, a: Number, b: Number) -> Number:
        """Subtract b from a and store the result."""
        self.current_value = a - b
        return self.current_value

    def multiply(self, a: Number, b: Number) -> Number:
        """Multiply two numbers and store the result."""
        self.current_value = a * b
        return self.current_value

    def divide(self, a: Number, b: Number) -> float:
        """Divide a by b and store the result. Raises ValueError on division by zero."""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        self.current_value = a / b
        return self.current_value

    def clear(self) -> float:
        """Reset the current value to 0.0."""
        self.current_value = 0.0
        return self.current_value