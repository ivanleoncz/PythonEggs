#!/usr/bin/python3

binary = []

n = int(input("\nPlease, insert an INT number: "))

dividend = n
while dividend > 0:
    remainder = dividend % 2
    binary.append(str(remainder))
    dividend  = dividend // 2

binary.reverse()
print("Binary:","".join(binary))
