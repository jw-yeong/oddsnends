# python3 program
# Computes numbers raised to large exponents (modulo some m)

import re
import string
import math

# get input problem
print ("Factoring m by brute force")
print ("Type m:")
m = int(input())



for i in range (2, m):
    if (m%i == 0):
      print ("sol: ", i)
      break;





