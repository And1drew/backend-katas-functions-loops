#!/usr/bin/env python
"""Implements math functions without using operators except for '+' and '-' """

__author__ = "???"


def add(x, y):
    """Add two integers. Handles negative values."""
    return x + y


def multiply(x, y):
    """Multiply x with y. Handles negative values of x or y."""
    value = 0
    print(x)
    print(y)
    for _ in range(abs(y)):
        value = add(value, x)
    if y < 0:
        value = -value
    return value


def power(x, n):
    """Raise x to power n, where n >= 0"""
    value = 1
    for i in range(n):
        value = multiply(value, x)
    return value


def factorial(x):
    """Compute factorial of x, where x > 0"""
    value = 1
    for i in range(2, add(x, 1)):
        value = multiply(value, i)
    return value


def fibonacci(n):
    """Compute the nth term of fibonacci sequence"""
    sequence = [0, 1]
    for i in range(n + 1):
        value = add(sequence[-2], sequence[-1])
        sequence.append(value)
    return sequence[n]


if __name__ == '__main__':
    print(multiply(3, 3))
    pass
