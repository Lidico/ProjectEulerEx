"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
 The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
Evaluate the sum of all the amicable numbers under 10000.
"""
from functools import reduce
from pip._vendor.urllib3.connectionpool import xrange


def sumOfDivisors(n) :
    i = 1
    sumOfDivisors = 0
    while i < n :
        if (n % i == 0) :
            sumOfDivisors += i
        i = i + 1
    return sumOfDivisors

def amicableNumbers(n):
    listOfAmicables = []
    i = 30
    while True:
        temp = sumOfDivisors(i)
        if sumOfDivisors(temp) == i:
            amicable1 = temp
            amicable2 = i
            i = temp
            if amicable1 > n or amicable2 > n:
                break
            if amicable1 != amicable2:
                listOfAmicables.append(amicable1)
                listOfAmicables.append( amicable2)
        i += 1
    return reduce(lambda x, y: x + y, listOfAmicables)

print(amicableNumbers(10000))
