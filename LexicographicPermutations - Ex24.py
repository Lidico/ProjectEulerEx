"""
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3
and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:
012   021   102   120   201   210
What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""
import math
from pip._vendor.urllib3.connectionpool import xrange

def swapPositions(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list

def convert(s):
    str1 = ""
    return (str1.join(s))

def lexicographicPermutation(n, numth):
    if n > 9 or n < 0:
        return 0
    digits = []
    for i in xrange(n+1):
        digits.append(str(i))
    if math.factorial(n+1) < numth:
        return 0
    if n == 1:
        if numth == 1: return 0
        else: return 1
    count = 1;
    while count < numth:
        i = n
        while digits[i - 1] >= digits[i]:
            i = i - 1;
        j = n+1;
        while (digits[j - 1] <= digits[i - 1]):
            j = j - 1;
        digits = swapPositions(digits, i - 1, j - 1);
        i += 1
        j = n+1;
        while i < j:
            digits = swapPositions(digits, i - 1, j - 1);
            i += 1
            j -= 1
        count += 1
    return convert(digits)

print(lexicographicPermutation(9,1000000))
