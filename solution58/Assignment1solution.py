import math

def factorial_math_library(n):
    return math.factorial(n)

# Test the function
number = int(input("Enter a number: "))
print(f"Factorial of {number} is {factorial_math_library(number)}")