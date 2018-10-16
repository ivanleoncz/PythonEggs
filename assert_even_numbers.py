#!/usr/bin/python3
""" Demonstrating the usage of assertions (sanity-check). """


def even_or_odd(n):
    try:
        assert n > 0, "Number must be greater than zero."
        if n % 2 == 0:
            return "Is Even."
        else:
            return "Is Odd."
    except AssertionError as e:
        return e


num = int(input("Insert a positive integer: "))
print(even_or_odd(num))
