#!/usr/bin/python3
""" Demonstrates Unit Test functionality. """

__author__ = "@ivanleoncz"

import unittest

class Calculator(unittest.TestCase):
    """ Contains basic arithmetic operations. """


    def test_addition(self, n1=3, n2=3):
        """ Calculates the addition of two numbers.
        
        Return: n1 + n2 """
        return n1 + n2

    
    def test_subtraction(self, n1=3, n2=3):
        """ Calculates the subtraction of two numbers.
        
        Return: n1 - n2 """
        return n1 - n2


    def test_multiplication(self, n1=3, n2=3):
        """ Calculates the multiplication of two numbers.
        
        Return: n1 * n2 """
        return n1 * n2


    def test_division(self, n1=3, n2=3):
        """ Calculates the division of two numbers.
        
        Return: n1 / n2 """
        return n1 / n2


if __name__ == "__main__":
    unittest.main()
