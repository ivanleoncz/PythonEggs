#!/usr/bin/python3
""" Demonstrates the usage of pop() built-in. """

fruits = ['banana','apple','pineapple']
print("The fruits that I have are: ", fruits)
consumed = fruits.pop(1)
print("I ate a: ", consumed)
print("Now I have: ", fruits)
