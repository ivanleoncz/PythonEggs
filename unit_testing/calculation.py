import time

class Calc:
    """ Arithmetic Operations for two numbers, per function. """
    
    def add(self, n1, n2):
        """ Performs addition of two numbers, at a time. """
        time.sleep(5) # intentional sleep for measuring time consumed
        return n1 + n2
      
    def sub(self, n1, n2):
        """ Performs subtraction of two numbers, at a time. """
        return n1 - n2
      
    def mult(self, n1, n2):
        """ Performs multiplication of two numbers, at a time. """
        return n1 * n2
      
    def div(self, n1, n2):
        """ Performs division of two numbers, at a time. """
        return n1 // n2
