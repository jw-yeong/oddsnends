# python3 program
# find inverse of a mod b
# brute force because anything non-naive is too much work
# yes you can always do the reverse euclidean algo but. . .meh
# you use this if your prof doesn't allow wolfram alpha

import re
import string
import math

def inverse(a, b):
    for i in range (1, b):
        if (i*a)%b==1:
            return i
    print ("inverse fail")
    return 0

# get input problem
print ("Solving g^-1 (mod m) with brute force instead of reverse Euclid.")
print ("Type g:")
g = int(input())
print ("Type modulus m:")
m = int(input())
print ("Solving for", g, "^ -1 (mod", m, ")")

#compute n
solution = inverse(g, m)
print ("sol:", solution)




