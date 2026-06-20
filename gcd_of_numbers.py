# Find GCD of two numbers.


# GCD :  Greates Common Divisor for two numbers. A largest positive number that divides
#        two numbers without leaving a remainder.


# 1. using Python built-in gcd method.

import math

a = 12
b = 18

result = math.gcd(a, b)
print("GCD :", result)


# 2. using Logic

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

print("GCD :", gcd(20, 18))