#!/usr/bin/python3

l = ["p","y","t"]
print("* List:                      ",l)

l += ["h","o","n"]
print("* List Increment:            ",l)

l = l * 2
print("* List Double:               ",l)

new_l = l[:]
print("* List Copy:                 ",new_l)

l.reverse()
print("* List Palindrome (reverse): ",l)

l.sort()
print("* List Sort:                 ", l)

print("* Min. Char (Alphabetical):  ", min(l))
print("* Max. Char (Alphabetical):  ", max(l))
print("* Count 'y':                 ", l.count("y"))
