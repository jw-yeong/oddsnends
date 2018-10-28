#python3 program
import re
import string


def gcd (a, b):
    if (b > a):
        print (euclid(b, a))
    else:
        print (euclid (a, b))

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
        euclid (b, r)


print ("Finding gcd (a,b). Type a:")
a = int(input())
print ("Type b:")
b = int(input())
gcd (a, b)