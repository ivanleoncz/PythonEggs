#!/usr/bin/python3
""" Demonstrating slicing. """

l = ["p","y","t","h","o","n"]
print("\nList:",l)
print("\nSlices:")
print("* first index:                              ",l[0])
print("* from index 0 to index 1:                  ",l[:2])
print("* from index 2 to end of list:              ",l[2:])
print("* from index 1 to penultimate index:        ",l[1:-1])
print("* from index 0 to end of list (incr. by 2): ",l[::2])
print("* everything, except last two items:        ",l[:-2])
print("* only the last two items:                  ",l[-2:])
print("* last index:                               ",l[-1])
print("* list palindrome:                          ",l[::-1])
