#!/usr/bin/python3

# main.py
if __name__ == "__main__":
    """Print the sum, difference, multiple and quotient of 10 and 5."""
from calculator_1 import add, subtract, multiply, divide

a = 10
b = 5

result_add = add(a, b)
result_subtract = subtract(a, b)
result_multiply = multiply(a, b)
result_divide = divide(a, b)

print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} - {} = {}".format(a, b, sub(a, b)))
    print("{} * {} = {}".format(a, b, mul(a, b)))
    print("{} / {} = {}".format(a, b, div(a, b)))
