
""" Define a class which has at least two methods:
        getString: to get a string from console input
        printString: to print the string in upper case

    Also please include simple test function to test the class methods.
"""

class Strings(object):

    def __init__(self):
        self.some_string = None

    def getString(self):
        self.some_string = input("Insert a string, please: ")

    def printString(self):
        print(self.some_string)

s = Strings()
s.getString()
s.printString()
