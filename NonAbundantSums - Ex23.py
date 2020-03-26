"""
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28,
 which means that 28 is a perfect number.
A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.
As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16,
the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers.
 However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.
Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""
import math
from pip._vendor.urllib3.connectionpool import xrange

def sumOfDivisors(n):
    result = 0
    i = 2
    while i <= (math.sqrt(n)):
        if (n % i == 0):
            if (i == (n / i)):
                result = result + i;
            else:
                result = result + (i + n / i);
        i = i + 1
    return int(result + 1);

def Remove(duplicate):
    final_list = []
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
    return final_list

def nonAbundantSums():
    abundantNums = []
    abundantNumsSumOfTwo = []
    sumOfNonAbundants = 0
    for i in xrange(12, 28123):
        sumsOfI = sumOfDivisors(i)
        if sumsOfI > i:
            abundantNums.append(i)
    for i in xrange(0,len(abundantNums)):
        for j in xrange(0, len(abundantNums)):
            abundantNumsSumOfTwo.append(abundantNums[i]+abundantNums[j])
        if abundantNums[i]+abundantNums[j] > 28123:
            break
    abundantNumsSumOfTwo = Remove(abundantNumsSumOfTwo)
    for i in xrange(1, 2**32):
        if len(abundantNumsSumOfTwo) == 0:
            break
        if i >= 2**32:
            break
        if i == abundantNumsSumOfTwo[0]:
            abundantNumsSumOfTwo.pop(0)
        else:
            sumOfNonAbundants += i
    return sumOfNonAbundants


print(nonAbundantSums())