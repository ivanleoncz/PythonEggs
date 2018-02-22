#!/usr/bin/python3

def is_leap(year):
    leap = False
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                leap = True
                return leap
            else:
                return leap
        else:
            return leap
    else:
        return leap

year = int(input("\nInsert a year, starting from 1990: "))

if year >= 1990:
    print(is_leap(year))
else:
    print("Year must start from 1990.")
