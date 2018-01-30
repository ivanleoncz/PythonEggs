#!/usr/bin/python3

x = 25
epsilon = 0.01

numGuesses = 0

low = 1.0
high = x
ans = (high + low) / 2.0

while abs(ans**2 - x) >= epsilon:
    print("\nlow: {0:<9}   high: {1:<9}   ans: (high+low)/2 == {2}".format(low,high,ans))
    numGuesses += 1
    if ans**2 < x:
        print("R:",ans, "squared is LESS than", x)
        low = ans
    else:
        print("R:",ans, "squared is GREATER than", x)
        high = ans
    ans = (high + low) / 2.0

print("\nnumGuesses = ",numGuesses)
print(ans, 'is close to square root of ',x)
