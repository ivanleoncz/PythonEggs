#!/usr/bin/python3
""" Adding data to lists. """

# empty list
l = []

# append to list
l.append("Python")
l.append(3.4)
l.append({"Author":"Guido van Rossum"})
l.append(["Computer Science","Web Development","Geoprocessing"])
print(l)

# inserting data at index 2
l.insert(2,1991)
print(l)

# concatenating lists
l.extend([{"Age":27},"Python Software Foundation"])
print(l)

