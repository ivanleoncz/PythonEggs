
import string
from json import dumps

lower = list(string.ascii_lowercase)
lower_caesar = lower[:]
upper = list(string.ascii_uppercase)
upper_caesar = upper[:]

rotate = int(input("Number of rotations: "))
word = input("Word to encrypt: ")

caesar_map = {}

for i in range(rotate):
    move_end = lower_caesar.pop(0)
    lower_caesar.append(move_end)
    move_end = upper_caesar.pop(0)
    upper_caesar.append(move_end)

for k, v in zip(lower, lower_caesar):
    caesar_map[k] = v

for k, v in zip(upper, upper_caesar):
    caesar_map[k] = v

caesar_word = ''
for letter in word:
    caesar_word += caesar_map[letter]
    

print("Caesar Map:\n{0}".format(dumps(caesar_map, indent=4)))
print("Encrypted Word:\n{0}".format(caesar_word))
