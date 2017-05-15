# CA5_10355283_MaryO'Sullivan
# Calculator using R


# This calculator has 10 functions:
# add, subtract, multiply, divide, 
# squareroot, square, factorial,
# sine, cosine, tangent



# This removes all variables from the environment 
rm(list=ls()) 				

# Functions

# This function takes two variables and adds them together
add <- function(x, y) {			
  return(x + y)
}

print(add(5,3))

# This function takes two variables and subtracts them 
subtract <- function(x, y) {
  return(x - y)
}

print(subtract(5,3))

# This function takes two variables and multiplies them 
multiply <- function(x, y) {
  return(x * y)
}

print(multiply(5,3))

# This function takes two variables and divides them
# It also retruns an error when the second variables 
# is zero

divide <- function(x,y) {
  if(y == 0){
    return ("error")
  } else {
    return(x/y)
  }
}

print(divide(5,3))

# This function takes one variable 

squareroot <-function(x) {
  return (sqrt(x))
}

print (squareroot(9))

# This function takes one variable
square <-function(x) {
  return (x*x)
}

print (square(9))

# This function takes one variable
# It also prints a message when 
# a negative number is selected

getfactorial <- function(num) {
  if(num < 0) {
    print("Sorry, factorial does not exist for negative numbers")
  } else if(num == 0) {
    print("The factorial of 0 is 1")
  } else {
    factorial = 1
    for(i in 1:num) {
      factorial = factorial * i
    }
    print(paste("The factorial of", num ,"is",factorial))
  }
}

print (getfactorial(5))

# This function takes one variable
# This returns the sine of x radians

sine <- function(x) {
  return(sin(x*pi/180))
}

print (sine(120))

# This function takes one variable
# This returns the cosine of x radians

cosine <- function(x) {
  return(cos(x*pi/180))
}

print (cosine(120))

# This function takes one variable
# This returns the tangent of x radians

tangent <- function(x) {
  if(x %% 180 ==0){
    return (0)
  } else if(x%% 90 ==0){
    return ("error")
  } else {
    return (tan(x*pi/180))
  }
}

print (tangent(90))
print (tangent(180))
print (tangent(50))

# User Input Function

# Get input from user.
# Option 1 takes input for functions that require 2 variables
# Option 2 takes input for functions that require 1 variable

getnumberinputs <- function() 
{ 
  numinputs = as.numeric(readline("Enter number of variables [1 or 2]: "))
  if (numinputs == 1) {
    print("Please select operation:")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    choice = as.integer(readline(prompt="Enter choice[1/2/3/4]: "))
    
    num1 = as.integer(readline(prompt="Please enter your first number: "))
    num2 = as.integer(readline(prompt="Please enter your second number: "))
    
    operator <- switch(choice,"+","-","*","/")
    result <- switch(choice, add(num1, num2), subtract(num1, num2), multiply(num1, num2), divide(num1, num2))
    
    print(paste(num1, operator, num2, "=", result))
  } else if (numinputs == 2) {
    print("Please select operation:")
    print("1.SquareRoot")
    print("2.Square")
    print("3.Factorial")
    print("4.Sine")
    print("5.Cosine")
    print("6.Tan")
    choice = as.integer(readline(prompt="Enter choice[1/2/3/4/5/6]: "))
    
    uinput = as.integer(readline(prompt="Please enter your input: "))
    operator <- switch(choice,"SquareRoot","Square","Factorial","Sine","Cosine","Tan")
    result <- switch(choice, squareroot(uinput), square(uinput), getfactorial(uinput), sine(uinput), cosine(uinput), tangent(uinput))
    print(paste(operator, uinput, "=", result))
  } else {print("invalid")}
  ask = readline(prompt="Would you like to do another calculation? Press y or any key ")
  if (ask != "y" )
    loop <- FALSE
  print("Goodbye!")
} 


#Calling the User Input  function
inptnumber <-getnumberinputs()



