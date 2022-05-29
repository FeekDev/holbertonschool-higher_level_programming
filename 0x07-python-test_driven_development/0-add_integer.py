#!/usr/bin/python3
"""
This Module adds two integers
...
teh purpose write a functions that adds 2 integers
"""

def add_integer(a, b=98):
    """
    Parameters: a and b both must be integers or float
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    elif type(b) not in [float, int]:
        raise TypeError("b must be an integer")
    else:
        return int(a + b)
    