#!/usr/bin/python3
""" Demonstration of multiplication table, using map and lambda. 

A list of numbers is passed as parameter to map() function, and 
a lambda function is applied (iteratively) to each element 
of the list, where each element dynamically corresponds to x.

The result generated via map() is converted into a list 
"""

__author__ = "@ivanleoncz"

numbers  = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
multiplier = int(input("\nInsert a number (0 to 9): "))
table = list(map(lambda n: multiplier * n, numbers))
print("Table:", table,"\n")
