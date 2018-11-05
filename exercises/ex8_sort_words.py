"""Write a program that accepts a comma separated sequence of words as input
and prints the words in a comma-separated sequence after sorting them
alphabetically.

Suppose the following input is supplied to the program:
without,hello,bag,world

Then, the output should be:
bag,hello,without,world
"""

words = input("Insert a list of words, separated by comma, please: ")

words_list = words.split(",")
words_list.sort()

print(",".join(words_list))
