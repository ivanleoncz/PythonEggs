#!/usr/bin/python3
""" Calculates the size of the hypotenuse of a right triangle,
using the Pythagorean Theorem.

a**2 + b**2 = c**2 

Basically, the theorem says:
    - the sum of the squares of the legs, is equal
    to the square of the hypotenuse
"""

from math import sqrt

__author__ = "@ivanleoncz"


def hypotenuse_calc():
    """ Calculates the hypotenuse. """
    leg_a = int(input("\nSize of leg A: "))
    leg_b = int(input("Size of leg B: "))
    squared_a = leg_a ** 2
    squared_b = leg_b ** 2
    hypotenuse_c = squared_a + squared_b
    return "Hypotenuse: %s " % int(sqrt(hypotenuse_c))


print(hypotenuse_calc(),"\n")
