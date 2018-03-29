#!/usr/bin/python3
""" Sums all positive integers contained in a range of numbers. 

Notice: only while loop is allowed for solving the problem.
"""

limit  = int(input("\nInsert a positive integer, please: "))
total  = 0
number = 1
while number <= limit:
    total  += number  # increments by the current number
    number += 1       # updates the number for while condition

print("\nSum of all numbers between 1 and {0}: {1}".format(limit,total))
