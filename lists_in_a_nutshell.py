#!/usr/bin/python3

l = []
print("Empty list:", l)

print("\n>>> APPENDING & REMOVING")
l.append("Python")
l.append("Node.js")
print("Appended values: \033[1;32m", l, "\033[1;m")
l.insert(1,"JavaScript")
print("Value inserted at index 1: \033[1;32m", l, "\033[1;m")
l.extend(["Java", "Ruby", "C"])
print("Extending (appending multiple values): \033[1;32m", l, "\033[1;m")
l.remove("Ruby")
print("Removed data by value 'Ruby': \033[1;32m", l, "\033[1;m")
l.pop(4)
print("Removed data by index 4: \033[1;32m", l, "\033[1;m")

print("\n>>> VALUES & INDEXES")
print("Value of first index: \033[1;32m", l[0], "\033[1;m")
print("Value of last index: \033[1;32m", l[-1], "\033[1;m")
print("Index of value Java: \033[1;32m", l.index("Java"), "\033[1;m")

print("\n>>> SLICING")
print("First and Last indexes: \033[1;32m", l[1:-1], "\033[1;m")
print("Two by Two: \033[1;32m", l[::2], "\033[1;m")
print("Last two items: \033[1;32m", l[:-2], "\033[1;m")
print("All, except the last two items: \033[1;32m", l[-2:],"\033[1;m")
print("Reversed list (palindrome): \033[1;32m", l[::-1], "\033[1;m")
print("Reversed list (two by two): \033[1;32m", l[::-2], "\033[1;m")

print("\n>>> REVERSING & SORTING")
l.reverse()
print("Reverse: \033[1;32m", l, "\033[1;m")
l.sort()
print("Sort: \033[1;32m", l, "\033[1;m")

print("\n>>> COUNTERS")
print("Length: \033[1;32m", len(l), "\033[1;m")
print("Number of 'Java' ocurrences: \033[1;32m", l.count("Java"), "\033[1;m")
print(min(l))
print(max(l))
