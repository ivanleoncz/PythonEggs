#!/usr/bin/python3
""" Adding data to lists. """

l = ["Python","JavaScript","Java","Go","C"]
print(l)

# removing by data
l.remove("Go")
print(l)

# removing by index
output = l.pop(1)
print(l)

# pop() returns the data which was removed
print("Removed:",output)
