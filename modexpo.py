# python3 program
# Computes numbers raised to large exponents (modulo some m)

import re
import string
import math

# get input problem
print ("Computing a^b mod m by brute force, because your prof prohibited wolfram alpha")
print ("Type a:")
a = int(input())
print ("Type b:")
b = int(input())
print ("Type modulus m:")
m = int(input())
print ("Solving for", a, "^", b, "(mod", m, ")")

solution = a
for i in range (b+1):
    solution=(solution**a)%m
print ("sol", solution)





