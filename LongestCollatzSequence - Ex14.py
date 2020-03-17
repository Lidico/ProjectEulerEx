""" The following iterative sequence is defined for the set of positive integers:
n → n/2 (n is even)
n → 3n + 1 (n is odd)
Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
Which starting number, under one million, produces the longest chain?
NOTE: Once the chain starts the terms are allowed to go above one million. """

from pip._vendor.urllib3.connectionpool import xrange
import time


def longestCollatzsequence():
    start = time.time()
    maxChainLong = 0
    highestNum = -1
    for i in xrange(999999, 99999, -2):
        curNum = i
        countChain = 1
        while curNum > 1:
            if curNum % 2 == 0:
                curNum = curNum/2
            else:
                curNum = 3*curNum+1
            countChain += 1
        if countChain > maxChainLong:
            highestNum = i
            maxChainLong = countChain
    end = time.time()
    print(end - start)
    return (highestNum, maxChainLong)

print(longestCollatzsequence())
