import sys
import fractions
import math
from functools import reduce
import time

p1=64553
q1=44159

p2=45823
q2=34583

p3=40231
q3=36739

# The crt algorithm is from https://www.geeksforgeeks.org/ by Nikita Tiwari.

def inv(a, m) :
    m0 = m
    x0 = 0
    x1 = 1
 
    if (m == 1) :
        return 0
 
    # Apply extended Euclid Algorithm
    while (a > 1) :
        q = a // m
        t = m
        m = a % m
        a = t
        t = x0
        x0 = x1 - q * x0
        x1 = t
    if (x1 < 0) :
        x1 = x1 + m0
 
    return x1
 
# k is size of num[] and rem[].
# Returns the smallest
# number x such that:
# x % num[0] = rem[0],
# x % num[1] = rem[1],
# ..................
# x % num[k-2] = rem[k-1]
# Assumption: Numbers in num[]
# are pairwise coprime
# (gcd for every pair is 1)
def findMinX(num, rem, k) :
    # Compute product of all numbers
    prod = 1
    for i in range(0, k) :
        prod = prod * num[i]
    result = 0
    for i in range(0,k):
        pp = prod // num[i]
        result = result + rem[i] * inv(pp, num[i]) * pp
     
     
    return result % prod
 

st = time.time()

#466921883457309
print("finding m^e for 46692")

rem = [1904996790,1005961829 ,1125160078]
num = [2850595927,1584696809 ,1478046709]
k = len(num)
print( "x is " , findMinX(num, rem, k))
 
print("finding m^e for 18834")

rem = [521785274 ,1504430603  ,725669205]
print( "x is " , findMinX(num, rem, k))


print("finding m^e for 57309")

rem = [1357610971,1583389928 ,1402930591]
print( "x is " , findMinX(num, rem, k))

et = time.time()
total_time = et - st
print('Execution time:', total_time, 'milliseconds')



