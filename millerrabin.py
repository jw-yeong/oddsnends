# python3 program
# Miller Rabin Test

import re
import string
import math

#expomod function
def expomod(a, b, n):
    sol = a
    #b-1 multiplications, just as a^2 is one multiplication
    for i in range (b-1):
        sol = (sol*a)%n
    return sol

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
    # end of algorithm, remainder is
    elif (b == 0):
        return a
    elif (b>1):
        q = a//b # floor division. in python2, this should be q = a/b
        r = a-b*q
        #print (a,"=",b,"x",q,"+",r)
        return euclid (b, r)

#Given n, returns largest q s.t. n = (2^k)q
def oddfactor(n):
    if (n%2 == 0):
        return oddfactor(n//2)
    return n

#Given n, returns largest k s.t. n = (2^k)q
def twopower(n):
    if (n%2 == 0):
        return 1 + twopower(n/2)
    return 0




#miller rabin test function
def millerrabin(n, a):
    if (n%2 == 0 or ((1 < gcd (a, n)) and (gcd(a, n) < n)) ):
        return ("n obviously composite")
    q = oddfactor(n-1)
    k = twopower(n-1)
    #A = (a**q)%n might cause memory problems, so instead:
    A = expomod(a, q, n) #A = a^q mod N
    if (A==1):
        return "TEST FAILS, try another witness"
    for i in range (0, k):
        if (A == n-1):
            return "TEST FAILS, try another witness"
        A = (A**2)%n
    return "n composite"
    

# get input problem
print ("Running Miller Rabin Test for Primality")
print ("Type number to be tested, n:")
n = int(input())
# 10 witnesses, i.e. 1 to N
N = 10

# test 1 to N as potential witnesses
for a in range (1, N+1):
    print (millerrabin(n, a))






