#!/usr/bin/python3

from functools import reduce

numbers = [1, 2, 3, 4, 5]
print("\nNumbers:", numbers, "\n")

squared = list(map(lambda x: x**2, numbers))
evens = list(filter(lambda x: x % 2 == 0, numbers))
sum_of_all = reduce(lambda x, y: x+y, numbers)

print("- squared:", squared)
print("- even numbers:", evens)
print("- sum of all numbers:", sum_of_all)
