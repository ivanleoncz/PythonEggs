#!/usr/bin/python3
""" Representing integer numbers as binary numbers. """

__author__ = "@ivanleoncz"


def int_to_bin(dividend):
    # if new dividend is equal to zero, stop calculation
    if dividend != 0:
        # calcularing remainder based on the current dividend
        remainder = dividend % 2
        # appending remainder (0 || 1) to list
        binary.append(str(remainder))
        # calculating new dividend for next recursion step
        dividend = dividend // 2
        # performing recursion with a new dividend
        return int_to_bin(dividend)


binary = []
n = int(input("\nInteger: "))
int_to_bin(n)
binary.reverse()
print("Binary: ","".join(binary))

