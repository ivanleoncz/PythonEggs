#!/usr/bin/python3

print("\n  Objective: a for loop that sums the values 1 through end variable.")
print("    Ex.: end = 6, then: 1 + 2 + 3 + 4 + 5 + 6 == 21")
print("\n  A variable called end, receives a random int number. \
\n  If end == 6, a for loop goes until the sixth position (6th), \
\nwhich is the number 5, not number 6. That's why a '+ 1' \
\nis added to sum of the proposed number for end.\n")

end = 6
s = 0
print("Proposed number for end: ", end)
print("Calculating...")
for n in range(end+1):
    s = s + n

print("Sum of all numbers including the number of end: ",s,"\n")
