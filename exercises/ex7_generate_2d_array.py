""" Write a program which takes 2 digits, X,Y as input and generates
a 2-dimensional array.

The element value in the i-th row and j-th column of the array should be i*j.

Note: i=0,1.., X-1; j=0,1,¡­Y-1.

Suppose the following inputs are given to the program:
3,5

Then, the output of the program should be:
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]] 
"""
import json

numbers = input("Insert dimensions for a 2-d array (separated by commas): ")
numbers = numbers.split(',')

lines = int(numbers[0])
columns = int(numbers[1])

array = list()

for i in range(0, lines):
    # 0 * "all numbers" from the next iteration 'n append each in a list
    # 1 * "all numbers"...
    # 2 * "all numbers"...
    # ...
    line = list()
    for j in range(0, columns):
        line.append(i * j)
    array.append(line)

for l in array:
    print(l)
