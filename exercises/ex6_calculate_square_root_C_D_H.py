""" Write a program that calculates and prints the value according
    to the given formula:
        Q = Square root of [(2 * C * D)/H]

    Following are the fixed values of C and H:
        C is 50.
        H is 30.

    D is the variable whose values should be input to your program in a
    comma-separated sequence.
    
    [EXAMPLE]

    Let us assume the following comma separated input sequence is given:
    100,150,180
    
    The output should be:
    18,22,24
"""

import math

C = 50
D = input("\nList of numbers (separated by commas), please: ")
H = 30

numbers = list()

for n in D.split(','):
    calc = int(round(math.sqrt((2 * C * int(n)) / H)))
    numbers.append(str(calc))

print(','.join(numbers))
