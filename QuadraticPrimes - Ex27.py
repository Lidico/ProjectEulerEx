"""
Euler discovered the remarkable quadratic formula:
n^2+n+41
It turns out that the formula will produce 40 primes for the consecutive integer values 0≤n≤39
0≤n≤39. However, when n=40,402+40+41=40(40+1)+41
n=40,
40^2+40+41=40(40+1)+41 is divisible by 41, and certainly when n=41,412+41+41
n=41, 41^2+41+41 is clearly divisible by 41.

The incredible formula n2−79n+1601
n^2−79n+1601 was discovered, which produces 80 primes for the consecutive values 0≤n≤79
0≤n≤79. The product of the coefficients, −79 and 1601, is −126479.
Considering quadratics of the form:

n2+an+b
n^2+an+b, where |a|<1000|a|<1000 and |b|≤1000 |b|≤1000

where |n||n| is the modulus/absolute value of n

e.g. |11|=11|11|=11 and |−4|=4|−4|=4
Find the product of the coefficients, a
a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of nn, starting with n=0
n=0.
"""

import math
from pip._vendor.urllib3.connectionpool import xrange


def isPrime(num):
    prime = True
    if num < 2: return False
    if num == 2: return True
    for factor in range(3,int(math.sqrt(num)),2):
        if num % factor == 0: prime = False
    return prime

def howManyPrimes(a, b):
    n = 0
    while True:
        if isPrime(n**2 + n*a + b):
            n += 1
        else:
            break
    return n

def quadraticPrimes(limitNum):
    bestValue = (-limitNum*2,-limitNum*2,0)
    for a in xrange(-limitNum, limitNum+1):
        for b in xrange(-limitNum, limitNum+1):
            n = howManyPrimes(a, b)
            if n > bestValue[2]:
                bestValue = (a, b, n)
    return bestValue

x = quadraticPrimes(1000)
print('the best a is: ', x[0], 'and best b is: ', x[1] , 'with ',x[2], ' primes')


