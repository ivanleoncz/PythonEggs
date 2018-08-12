#!/usr/bin/python3


number = int(input("\nFactorial of: "))

result = number

for n in range(number - 1, 0, -1):
    result *= n

print("Result:", result, "\n")
