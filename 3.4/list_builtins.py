#!/usr/bin/python3
''' Demonstrating some built-ins for list data types.'''


l = [3,5,2,0,4,5,7,3,1,6,23,4,9,2,4]

print("\nList:",l)
l.append(25)
print("\nList (appended number 25):",l)
l.pop(0)
print("List (index 0 removed):",l)
l.sort()
print("List (sorted):",l)
l.reverse()
print("List (reversed):",l)
print("List (returns first index ocurrence of value 3):",l.index(3))
print("List (count ocurrences of value 4):",l.count(4))

