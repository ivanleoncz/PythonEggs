#!/us/bin/python3

from functools import reduce

numbers = [2, 3, 4, 5, 6]
print("\nNumbers:", numbers, "\n")

even_numbers = list(filter(lambda x: x % 2 == 0, numbers ))
sum_even_numbers = reduce(lambda x, y: x + y, even_numbers )

print("Result:", sum_even_numbers)
