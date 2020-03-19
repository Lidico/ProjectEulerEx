"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
"""
from functools import reduce

from pip._vendor.urllib3.connectionpool import xrange


def numberLetterCounts(n):
    if n > 1000: return -1
    letterCount = 0
    LISTOFUNITSCOUNT = [3,3,5,4,4,3,5,5,3,3]
    LISTOF1XCOUNTS = [6,6,8,8,7,7,9,9,8]
    LISTOFTENSCOUNT = [6,6,5,5,5,7,6,6]
    HUNDREDCOUNT = 7
    THOUSANDCOUNT = 8
    ANDCOUNT = 3

    letterCount += reduce(lambda x, y: x + y, LISTOFUNITSCOUNT)
    letterCount += reduce(lambda x, y: x + y, LISTOF1XCOUNTS)
    for i in xrange(20,n+1):
        curNum = str(i)
        if len(curNum) == 2:
            letterCount += LISTOFTENSCOUNT[int(curNum[0])-2]
            if int(curNum[1]) != 0:
                letterCount += LISTOFUNITSCOUNT[int(curNum[1])-1]
        elif len(curNum) == 3:
            letterCount += LISTOFUNITSCOUNT[int(curNum[0])-1] + HUNDREDCOUNT
            if int(curNum[1]) != 1:
                if int(curNum[1]) != 0 and int(curNum[2]) != 0:
                    letterCount += LISTOFTENSCOUNT[int(curNum[1])-2] + ANDCOUNT + LISTOFUNITSCOUNT[int(curNum[2])-1]
                elif int(curNum[1]) == 0 and int(curNum[2]) != 0:
                    letterCount += LISTOFUNITSCOUNT[int(curNum[2])-1] + ANDCOUNT
                else:
                    letterCount += LISTOFTENSCOUNT[int(curNum[1])-2] + ANDCOUNT
            else:
                if int(curNum[2]) == 0:
                    letterCount += LISTOFUNITSCOUNT[9] + ANDCOUNT
                else:
                    letterCount += LISTOF1XCOUNTS[int(curNum[2])-1] + ANDCOUNT
        else:
            letterCount += LISTOFUNITSCOUNT[0] + THOUSANDCOUNT
    return letterCount

print(numberLetterCounts(1000))