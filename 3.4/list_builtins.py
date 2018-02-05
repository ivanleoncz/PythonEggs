#!/usr/bin/python3
''' Demonstrating some built-ins for list data type.'''

l = [3,5,2,0,4,5,7,3,1,6,23,4,9,2,4]

print("\nLIST:",l)
l.append(25)
print("\n- appending number 25:",l)
l.pop(0)
print("- removing value from index 0:",l)
l.sort()
print("- sorting list:",l)
l.reverse()
print("- reversing list:",l)
print("- returning first index ocurrence of value 3:",l.index(3))
print("- count ocurrences of value 4:",l.count(4))
print("- length of list:",len(l))

