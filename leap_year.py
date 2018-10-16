#!/usr/bin/python3

def is_leap(year):
    leap = False
    if year % 4 == 0:
        leap = True
        if year % 100 == 0:
            leap = False
            if year % 400 == 0:
                leap = True
    return leap

year = int(input("\nInsert a year, starting from 1900: "))

if year >= 1900:
    print(is_leap(year))
else:
    print("Year must start from 1900.")
