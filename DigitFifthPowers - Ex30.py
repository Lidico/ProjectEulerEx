"""
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:
1634 = 14 + 64 + 34 + 44
8208 = 84 + 24 + 04 + 84
9474 = 94 + 44 + 74 + 44
As 1 = 14 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.
Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
"""
from pip._vendor.urllib3.connectionpool import xrange


def checkIfSumOfDigits(number, n):
    sum = 0
    lenOfNum = len(str(number))
    for i in xrange(lenOfNum):
        sum += float(str(number)[i])**n
    if int(sum) == number:
        return int(sum)
    else:
        return 0


def digitsFifthPowers(n):
    sumOfFifthPowers = 0
    for number in xrange(2, 354294):
        sumOfFifthPowers += checkIfSumOfDigits(number, n)
    return sumOfFifthPowers

print(digitsFifthPowers(5))
