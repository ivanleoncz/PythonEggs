#!/usr/bin/python3

total = 0
n = 1
while n <= 6:
    # total + the current iterator, starting by ZERO
    #  0 + 1 = 1
    #  1 + 2 = 3
    #  3 + 3 = 6
    #  6 + 4 = 10
    # 10 + 5 = 15
    # 15 + 6 = 21
    total += n     # 1  # 3  # 6  # 10  # 15  # 21
    n += 1         # 2  # 3  # 4  # 5   # 6   # 7
print(total)
