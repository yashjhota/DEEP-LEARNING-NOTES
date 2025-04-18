"""
    A calculator module that provides basic arithmetic operations.
"""

def add(a, b):
    """Return the sum of two numbers."""
    return a + b
def subtract(a, b):
    """Return the difference of two numbers."""
    return a - b
def multiply(a, b):
    """Return the product of two numbers."""
    return a * b
def divide(a, b):
    """Return the quotient of two numbers."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b
def power(a, b):
    """Return the result of raising a to the power of b."""
    return a ** b

