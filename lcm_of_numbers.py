# Find LCM of two numbers.

# LCM : Least Common Multiple. A smallest positive number that is multiple of both numbers


# 1. using python built-in function

import math

a = 12
b = 18

result = math.lcm(a, b)
print("LCM :", result)

# 2. using Logic

def gcd(c, d):
    while d != 0:
        c, d = d, c % d
    return c
# first compute GCD of two numbers

def lcm(c, d):
    return (c * d) // gcd(c, d)

print("LCM :", lcm(4, 8))