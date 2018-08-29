
import string
from json import dumps

alphabet = list(string.ascii_lowercase)
alphabet_caesar = alphabet[:]
rotate = int(input("Number of rotations: "))
word = input("Word to encrypt: ")

caesar_map = {}

for i in range(rotate):
#    move_beggining = alphabet_caesar.pop(-1)
#    alphabet_caesar.insert(0, move_beggining)
    move_end = alphabet_caesar.pop(0)
    alphabet_caesar.append(move_end)

for k, v in zip(alphabet, alphabet_caesar):
    caesar_map[k] = v

caesar_word = ''
for letter in word:
    caesar_word += caesar_map[letter]
    
print("Alphabet:\n{0}".format(alphabet))
print("Alphabet Caesar (rotate {0}):\n{1})".format(rotate, alphabet_caesar))
print("Caesar Map:\n{0}".format(dumps(caesar_map, indent=4)))
print("Encrypted Word:\n{0}".format(caesar_word))
