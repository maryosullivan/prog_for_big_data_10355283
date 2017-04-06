# Programming for Big Data: 10355283_Mary O'Sullivan 
# ca1_use-calculator_10355283
# This file allows the user to use the scientific calculator 

# This imports all functions from scientific calculator function file
from ca1_calculator_10355283 import *

# Function identifying menu options 
def show_menu():
    print '#######################\n'
    print '***Scientific Calculator***\n'
    print 'Select 1 for Addition'
    print 'Select 2 for Subtraction'
    print 'Select 3 for Multiplicaiton'
    print 'Select 4 for Division'
    print 'Select 5 for Exponent'
    print 'Select 6 to return the sine of x radians'
    print 'Select 7 to return the cosine of x radians'
    print 'Select 8 to return the tangent of x radians'
    print 'Select 9 to return the square root of x'
    print 'Select 10 to return the square of x\n'
    print 'Type Q to quit\n'
    print '#######################\n'
    
# Funtion to be called when invalid choice is made     
def invalid_choice_prompt():
    print 'Invalid choice'
    raw_input('Please press enter to return to the main menu\n')
   
# while Loop - continue in calculator until the user selects to quit
while True:
    show_menu()                                                                                     # Menu presented to User indicating options available to him/her, including an option to quit the calculator.                                                                                        
    s_input = raw_input('Please select an option from the Scientific Calculator menu:\n').lower()   # Input request with option to quit and return to the main menu
    if s_input == 'q':
        break
    try:                  
        choice = float(s_input)
    except: 
        invalid_choice_prompt()                          # Call function to prompt the user that they made an invalid choice and to return to the main menu
        continue
        
    if choice < 1 or choice > 10:                        # Where the selection made is outside that of the menu, call invalid choice prompt function
        invalid_choice_prompt()
        continue        
    elif choice > 5 and choice < 11:                    # Where the menu selection made is 6,7,8,9 or 10, prompt user to enter 1 number (1 parameter for these calculator functions) 
        num1 = float(raw_input('Enter first number '))
    else:                                               # For all other correct menu selections i.e. 1,2,3,4 or 5 prompt user to enter 2 numbers (2 parameters for these calculator functions)
        num1 = float(raw_input('Enter first number '))
        num2 = float(raw_input('Enter second number '))  
        

# Computations / Calculations  #Message statement and string.format()
    if choice == 1:                                                                         
        result = add(num1, num2)                                                            
        message = '{} plus {} equals {}'.format(num1,num2,result)                                    
    elif choice == 2:                                                                       
        result = subtract(num1, num2)                                                            
        message = '{} less {} equals {} '.format(num1,num2,result) 
    elif choice == 3:                                                                       
        result = multiply(num1, num2)                                                            
        message = '{} by {} equals {} '.format(num1,num2,result)   
    elif choice == 4:                                                                       
        result = divide(num1, num2) 
        if num2 == 0:
            message = 'Invalid Operation, you cannot divide by zero'
        else: 
            message = '{} divided by {} equals {}'.format(num1,num2,result)
    elif choice == 5:                                                                       
        result = exponent(num1, num2)                                                            
        message = '{} to the power of {} equals {} '.format(num1,num2,result)
    elif choice == 6:                                                                       
        result = calculate_sin(num1)                                                            
        message = 'The sin of {} equals {} '.format(num1,result)  
    elif choice == 7:                                                                       
        result = calculate_cos(num1)                                                            
        message = 'The cos of {} equals {} '.format(num1,result)  
    elif choice == 8:                                                                       
        result = calculate_tan(num1)                                                            
        message = 'The tan of {} equals {}'.format(num1,result)
    elif choice == 9:                                                                       
        result = calculate_sqroot(num1)                                                            
        message = 'The square root of {} equals {}'.format(num1,result)   
    elif choice == 10:                                                                       
        result = calculate_square(num1)                                                            
        message = '{} squared equals {}'.format(num1,result)          
    else:
        message = 'Invalid selection. Press enter to continue:\n'                           
    print message                                                                                   # One print statement
    
    s_input = raw_input('\nPlease press enter to return to the main menu or Q to quit:\n').lower()  # Input request with option to quit or return to the main menu
    if s_input == 'q':
        break   
        
print 'Thank you for using the Calculator'                                                          # When user quits the calculator, close loop and print this message 

    