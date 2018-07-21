#!/usr/bin/python3

start = 0
end = 100

answer = 26
guess = None

oper = 0

while True:

    guess = (start + end) // 2
    print("\nOperation:", oper)
    print("- start:", start)
    print("- end:  ", end)
    print("- guess:", guess)
    if guess > answer:
        end = guess
    elif guess < answer:
        start = guess
    elif guess == answer:
        print("The number is:", guess)
        break

    oper += 1


