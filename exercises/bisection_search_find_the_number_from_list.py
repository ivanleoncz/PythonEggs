#!/usr/bin/python3

import time


numbers = [2, 56, 90, 8076, 32, 46, 24, 13, 87, 7, 34, 923]
number = 24

start = 0
end = len(numbers) -1

counter = 0
numbers.sort()

while True:
    time.sleep(2)
    counter += 1
    print("\nAttempt:", counter)
    print("Slice:", numbers[start:end])
    idx = len(numbers[start:end]) // 2
    print("Index:", idx)
    guess = numbers[start:end][idx]
    print("Guess:", guess)
    if number == guess:
        print("Found it:", guess)
        break
    elif number < guess:
        end = idx
        print("Number is less than", guess)
    elif number > guess:
        start = idx
        print("Number is greater than", guess)
