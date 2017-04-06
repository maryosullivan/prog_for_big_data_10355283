# Programming for Big Data: 10355283_Mary O'Sullivan 
# ca1_test-calculator_10355283
# This file runs multiple tests for each of the 10 scientific calculator functions 

import unittest

from ca1_calculator_10355283 import *               # This imports all functions from scientific calculator function file 

class TestCalculator(unittest.TestCase):
    def testAdd(self):                              # This tests the Add function 
        self.assertEqual(add(2, 2), 4)              # 2 + 2 = 4
        self.assertEqual(add(5, 3), 7)              # 5 + 3 = 7: This will result in a Fail test notification with an AssertionError: 8 != 7 
        self.assertEqual(add(4, 0), 4)              # 2 + 2 = 4

    def testSubtract(self):                         # This tests the Subtract function
        self.assertEqual(subtract(2, 2), 0)         # 2 - 2 = 0
        self.assertEqual(subtract(5, 3), 2)         # 5 - 3 = 2 
        self.assertEqual(subtract(4, 0), 4)         # 4 - 0 = 4 

    def testMultiply(self):                         # This tests the Multiply function
        self.assertEqual(multiply(2, 2), 4)         # 2 * 2 = 4
        self.assertEqual(multiply(5, 3), 15)        # 5 * 3 = 15
        self.assertEqual(multiply(4, -1), -4)       # 4 * -1 = -4
        
    def testDivide(self):                           # This tests the Divide function
        self.assertEqual(divide(4, 1), 4)           # 4 / 1 = 4
        self.assertEqual(divide(4, 2), 2)           # 4 / 2 = 2
        self.assertEqual(divide(2, 2), 1)           # 2 / 2 = 1
        self.assertEqual(divide(0, 1), 0)           # 0 / 1 = 0
        self.assertEqual(divide(5, 4), 1.25)        # 5 / 4 = 1.25 = Returns a float as the function converts the second parameter to a float
        self.assertEqual(divide(4, 0), 'error')     # This will result in a Fail test notification with a ZeroDivisionError: float division by zero

    def testExponent(self):                         # This tests the Exponent function
        self.assertEqual(exponent(2, 2), 4)         # 2**2 = 4
        self.assertEqual(exponent(3, 0), 1)         # 3**0 = 1
        self.assertEqual(exponent(-3, 2), 9)        # -3**2 = 9   
        self.assertEqual(exponent(2.5, 2), 6.25)    # 2.5**2 = 6.25
        
    def testSin(self):                                          # This tests the Sin function
        self.assertEqual(calculate_sin(40), 0.6427876096865393) # Sin(40) = 0.6427876096865393
        self.assertEqual(calculate_sin(180), 0)                 # Sin(180) = 0
        self.assertEqual(calculate_sin(270), -1)                # Sin(270) = 0
     
    def testCos(self):                                          # This tests the Cos function
        self.assertEqual(calculate_cos(60), 0.5000000000000001) # Cos(60) = 0.5 
        self.assertEqual(calculate_cos(180), -1.0)              # Cos(180) = -1.0 
        self.assertEqual(calculate_cos(95), -0.0871557427474)   # Cos(95) = - 0.5 
    
    def testTan(self):                                          # This tests the Tan function
        self.assertEqual(calculate_tan(180), 0)                 # Tan(180) = 0 
        self.assertEqual(calculate_tan(50), 1.19175359259421)   # Tan(50) = 1.19119175359259421
        self.assertEqual(calculate_tan(270), 'Invalid Input')   # Tan(270) = This will return an error 
        self.assertEqual(calculate_tan(90), 'Invalid Input')    # Tan(90) = This will return an error 

    def testSqrt(self):                                         # This tests the Square Root function where x > 0 
        self.assertEqual(calculate_sqroot(9), 3.0)              # Square Root of 9 = 3.0 
        self.assertEqual(calculate_sqroot(72.5), 8.51469318296) # Square Root of 72.5 = 8.514693182963201 
        self.assertEqual(calculate_sqroot(16), 4.0)             # Square Root of 16 = 4.0

    def testSquare(self):                                       # This tests the Square function
        self.assertEqual(calculate_square(5), 25)               # 5^2 = 25
        self.assertEqual(calculate_square(1), 1)                # 1^2 = 1
        self.assertEqual(calculate_square(0), 0)                # 0^2 = 0
        self.assertEqual(calculate_square(-3), 9)               # -3^2 = 9
        self.assertEqual(calculate_square(6.5), 42.25)          # 6.5^2 = 42.25     
        
if __name__ == '__main__':
	unittest.main()
 