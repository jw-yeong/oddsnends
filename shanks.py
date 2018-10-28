# python3 program
# Implements Shanks's Baby Step Giant Step Algo to solve the DLP

import re
import string
import math


# find inverse of a mod b
# brute force because anything non-naive is too much work
# yes it defeats the purpose of Shanks, but we can always swap it out another day
def inverse(a, b):
    for i in range (1, b):
        if (i*a)%b==1:
            return i
    print ("inverse fail")
    return 0

# get input problem
print ("Solving DLP with Shanks's Baby Step Giant Step Algo.")
print ("Type g:")
g = int(input())
print ("Type h:")
h = int(input())
print ("Type prime p:")
p = int(input())
print ("Solving for", g, "^ x =", h, "(mod", p, ")")

#compute n
n = 1+math.floor(math.sqrt(p))
print ("n:", n)

#create babystep list e,g...,g^n
# note: index i contains g^i
babystep = []
for i in range (n+1):
    elt = (g**i)%p
    babystep.append(elt)
    print ("i:", i, "elt:", elt)

# create giantstep list h,hg^(-n),...hg^(-n*n)
# note: index k contains hg^(-kn)
giantstep = []
ginverse = inverse(g, p)
print ("inverse: ", ginverse)
giantstep.append(h)
for k in range (1, n+1):
    previouselt = giantstep[k-1] # hg^((-k-1)n)
    gtominusn = ginverse**n      # g^-n
    elt = previouselt*gtominusn  # hg^(-kn)
    giantstep.append(elt%p)
    print (elt%p)


# Strictly speaking, we should sort the lists for better runtime.
# However, notice that we have to deal with significantly more code:
# For one thing, we lose the handy invariants that index i contains g^i
# in the babystep list, and index k contains hg^(-kn) in the giantstep list.
# If we want to sort the lists, we need them to be lists of pairs,e.g.(g**i, i)
# or else we look at an elt g**i and we've completely forgotten what i is.
# Of course, this makes everything harder to code: it's harder to sort and compare
# because we're now dealing with a list of pairs instead of numbers.
# So I am taking the easy way out, and throwing runtime and elegance out the window,
# because an hours' debugging isn't worth a few extra points on HW.


# compare lists and find a match such that g^i = hg^(-kn)
# when a match is found, baby count is i, giantcount is k
i = 0;
k = 0;
for babycount in range(n+1):
    if (i!=0 and k!= 0): break;
    for giantcount in range(n+1):
        if (babystep[babycount] == giantstep[giantcount]):
            i = babycount
            k = giantcount
            break;

# x = kn+i solves g^x = h (mod p)
print ("solution:", k*n+i)



