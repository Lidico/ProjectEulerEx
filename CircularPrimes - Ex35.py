"""
The number, 197, is called a circular prime because all rotations of the digits:
197, 971, and 719, are themselves prime.
There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
How many circular primes are there below one million?
"""
from pip._vendor.urllib3.connectionpool import xrange
import sympy

def rotate(strg, n):
    return strg[n:] + strg[:n]

def checkIfCircular(num):
    count = 0
    strNum = str(num)
    for i in xrange(len(strNum)):
        if sympy.isprime(int(rotate(strNum,i*(-1)))):
            count +=1
    if count == len(strNum):
        return True
    else:
        return False

def checkIfAllDigitsIsOdd(num):
    strNum = str(num)
    for i in xrange(len(strNum)):
        if int(strNum[i])%2 == 0:
            return False
    return True

def circularPrimes(n):
    CIRCULARPRIMESUNDER100 = 13
    countCircular = 0
    arrOfPotentialCircular = []
    if n < 100: return CIRCULARPRIMESUNDER100
    for num in xrange(101, n, 2):
        if checkIfAllDigitsIsOdd(num):
            arrOfPotentialCircular.append(num)
    for num in arrOfPotentialCircular:
        if checkIfCircular(num):
            countCircular +=1
    return countCircular + CIRCULARPRIMESUNDER100

print(circularPrimes(1000000))