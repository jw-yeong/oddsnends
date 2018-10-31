# python3 program
# Pollard p-1 algo

import re
import string
import math

#expomod function
#implements (hopefully) memory-saving (a**b)%n
def slow_power(a, b, n):
    sol = a
    #b-1 multiplications, just as a^2 is one multiplication
    for i in range (b-1):
        sol = (sol*a)%n
    return sol


# fast power algo taken from:
# https://www.rookieslab.com/posts/fast-power-algorithm-exponentiation-by-squaring-cpp-python-implementation
def fast_power(base, power, mod):
    result = 1
    while power > 0:
        # If power is odd
        if power % 2 == 1:
            result = (result * base) % mod
        
        # Divide the power by 2
        power = power / 2
        # Multiply base to itself
        base = (base * base) % mod
    
    return result

#gcd function
def gcd (a, b):
    if (b > a):
        return euclid(b, a)
    else:
        return euclid (a, b)

#euclidean algorithm
#invariant that a > b
def euclid(a, b):
    # end of algorithm, remainder is 1, solution is other number.
    if (b == 1):
        return 1
    # end of algorithm, remainder is 0, solution is other number.
    elif (b == 0):
        return a
    elif (b>1):
        q = a//b # floor division. in python2, this should be q = a/b
        r = a-b*q
        #print (a,"=",b,"x",q,"+",r)
        return euclid (b, r)



# get input problem
print ("Running Pollard's p-1 factorization")
print ("Type number to be factorized, N:")
N = int(input())
print ("Type upper bound for testing, UB:")
upperbound = int(input())

a = 2
#for j in range (2, upperbound):
for j in range (2, upperbound):
    J = math.factorial(j) # also known as L in textbook. Optional step
    A = slow_power(a, J, N)
    print ("j = ", j,"J = ", J, "A = ", A)
    d = gcd(A-1, N)
    if (1 < d and d < N):
        print ("SUCCESS, d=", d)










