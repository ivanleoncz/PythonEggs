#!/usr/bin/python3
""" Maps even numbers from a list of numbers, using list comprehension
with filtering.
"""

__author__ = "@ivanleoncz"


numbers = [0, 3, 4, 11, 19, 38, 62, 176, 293, 306]

print("All Numbers:", numbers)
print("Even Numbers:", [n for n in numbers if n % 2 == 0])

