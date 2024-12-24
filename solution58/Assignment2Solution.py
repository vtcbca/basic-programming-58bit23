import math

def is_prime_math_library(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Test the function
number = int(input("Enter a number: "))
if is_prime_math_library(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")