"""
The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from
 left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left:
  3797, 379, 37, and 3.
Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""
from pip._vendor.urllib3.connectionpool import xrange
import sympy

def isTruncatable(num):
  for i in xrange(len(num)):
      tNum = num[i:]
      if sympy.isprime(int(tNum)) == False:
          return False
  for i in xrange(len(num)):
      tNum = num[:len(num)-i]
      if sympy.isprime(int(tNum)) == False:
          return False
  return True

def truncatablePrimes():
    count = 0
    sumOfTruncatable = 0
    num = 11
    while count < 11:
        strNum = str(num)
        if isTruncatable(strNum):
            sumOfTruncatable += num
            count += 1
        num += 1
    return sumOfTruncatable

print(truncatablePrimes())

