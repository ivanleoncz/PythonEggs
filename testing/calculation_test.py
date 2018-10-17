import calculation
import unittest

calc = calculation.Calc()

class Probe(unittest.TestCase):
    """ Probe for testing Calc class and its methods. """
    
    def test_add(self):
        """ Testing add() method from Calc class. """
        self.assertEqual(calc.add(3, 3), 6)
                                                                                
    def test_sub(self):
        """ Testing sub() method from Calc class. """
        self.assertEqual(calc.sub(3, 3), 0)
                                                                                
    def test_mult(self):
        """ Testing mult() method from Calc class. """
        self.assertEqual(calc.mult(3, 3), 9)
                                                                                
    def test_div(self):
        """ Testing div() method from Calc class. """
        self.assertEqual(calc.div(3, 3), 1)
        
if __name__ == "__main__":
    unittest.main()
