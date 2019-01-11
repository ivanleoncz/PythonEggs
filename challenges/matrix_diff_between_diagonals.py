#!/usr/bin/python3

pos = 0

matrix = [ [2, 5, 7], [5, 9, 7] , [3, 2, 1] ]

left_right = 0
right_left = 0

# sum left_right diagonal
for m in matrix:
    print("sub matrix: ", m)
    print("pos: ", pos)
    left_right += m[pos]
    pos += 1

pos -= 1

# sum right_left diagonal
for m in matrix:
    print("sub matrix: ", m)
    print("pos: ", pos)
    right_left += m[pos]
    pos -= 1


print("\n[Matrix] -> ", matrix)
print(" - left_right: ", left_right)
print(" - right_left: ", right_left)
print(" - difference: ", abs(left_right - right_left) )
