# CA1_Programming for Big Data: 10355283_Mary O'Sullivan 
# ca1_calculator_10355283
# This file defines 10 different scientific calculation functions

import math
# Addition Function; this takes two parameters 
def add(first, second):
	return first + second
    
# Subtraction Function; this takes two parameters 
def subtract(first, second):
	return first - second

# Multiplication Function; this takes two parameters; 
# Where one of the numbers is a zero it is display an "Error"    
def multiply(first, second):
    if second == 0:
        return 'Error'     
    return first * second

# Division Function; this takes two parameters;     
# To cater for floor division, I have converted the second parameter to a float.
def divide(first, second):
    if second == 0:
        result = 'Invalid operation. You cannot divide by zero'
    else:
        result = first / float(second)
    return result
    
# Exponent Function; this takes two parameters;         
def exponent(first, second):
    return first ** second

# Sin Function: this returns the sine of x radians; and takes 1 parameter   
def calculate_sin(x):
    sin = math.sin(math.radians(x))
    return sin
    
# Cos Function: this returns the cosine of x radians; and takes 1 parameter      
def calculate_cos(x):
    cos = math.cos(math.radians(x))
    return cos

# Tan Function: this returns the tangent of x radians; and takes 1 parameter       
def calculate_tan(x):
    if x % 180 == 0:
        tan = 0
    elif x % 90 == 0:
        tan = 'Invalid input'
    else:   
        tan = math.tan(math.radians(x))
    return tan
    
# Square Root Function: this returns the square root of x; and takes 1 parameter    
def calculate_sqroot(x):
    sqroot = math.sqrt(x)
    return sqroot
    
# Square Funtion: this calculates the square of x; and takes 1 parameter    
def calculate_square(x):
    square = x * x 
    return square
    