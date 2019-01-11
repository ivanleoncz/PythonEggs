#!/usr/bin/python3


numbers = [1, 1, 0, -1, -1]

def calc_fractions(arr):

    positives = 0
    negatives = 0
    zeroes = 0

    for n in arr:
        if n > 0:
            positives += 1
        elif n < 0:
            negatives += 1
        elif n == 0:
            zeroes += 1

    calc_pos = positives / len(numbers)
    calc_neg = negatives / len(numbers)
    calc_zer = zeroes / len(numbers)
    return "{0:.6f}\n{1:.6f}\n{2:.6f}".format(calc_pos, calc_neg, calc_zer)


print(calc_fractions(numbers))
