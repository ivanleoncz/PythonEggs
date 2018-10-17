#!/usr/bin/python3
""" Verifies which numbers from a list of postive integers are even, 
using filter and lambda. 

filter() constructs a list of elements which were successfully 
evaluated, according with the lambda function, upon the elements
of an iterable (list, strings, etc.).
"""

__author__ = "@ivanleoncz"

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 11]
even = filter(lambda n: n % 2 == 0, numbers)

print("Positive Integers: ", numbers)
print("Who is even:       ", list(even))
