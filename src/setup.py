# This is a simple calculator module that provides basic arithmetic operations.
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def subtract(a, b):
    return a - b

def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    return a / b

def power(a, b):
    return a ** b

def mod(a, b):
    return a % b