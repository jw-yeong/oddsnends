# python3 program
# Implements Pollard's rho-method, for midterm
import re
import string
import math

def gcd (a, b):
    if (b > a):
        euclid(b, a)
    else:
        euclid (a, b)

#euclidean algorithm
def euclid(a, b):
    if (b>1):
        q = a//b # floor division
        r = a-b*q
        #print (a,"=",b,"x",q,"+",r)
        euclid (b, r)

def mixer(x, N):
    int( ((int(x)**2)+1)%int(N) )

# get input problem
print ("Pollard's rho method.")
print ("Type N:")
N = int(input())

x0 = 0
y0 = 0

#create babystep list e,g...,g^n
# note: index i contains g^i
xseq = []
yseq = []
xseq.append(x0)
yseq.append(y0)
collision = False
while (not collision):
    xprev = xseq[-1]
    xi = mixer(int(xprev), N)
    xseq.append(xi)

    yprev = yseq[-1]
    fyprev = int (mixer(int(yprev), N))
    if (fyprev is None):
        print ("bug: fyprev is nonetype")
    yi = mixer(int(fyprev), N)
    yseq.append(yi)

    if (gcd (abs(xi-yi), N) != 1):
        print ("gk = p = ", gcd (abs(xi-yi), N) )
        collision = True




