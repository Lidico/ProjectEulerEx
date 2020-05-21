"""
Take the number 192 and multiply it by each of 1, 2, and 3:
192 × 1 = 192
192 × 2 = 384
192 × 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)
The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?
"""

def checkIfDiffrent(n):
    strNum = str(n)
    res = ''.join(sorted(strNum))
    if res[0] == '0':
        return False
    if len(set(strNum)) == len(strNum):
        return True
    else:
        return False

def pandigitalMultiples(n):
    listOfDigits = []
    for i in range(1, n+1):
        listOfDigits.append(str(i))
    maxNum = 0
    for number in range(1, 9999):
        curPandigital = ''
        for n in range(1, 9):
            if checkIfDiffrent(number*n) == False:
                break
            else:
                curPandigital+=str(number*n)
                if len(curPandigital) < 9:
                    if checkIfDiffrent(int(curPandigital)):
                        continue
                    else:
                        break
                elif len(curPandigital) > 9:
                    break
                else:
                    if checkIfDiffrent(curPandigital):
                        maxNum = max(maxNum, int(curPandigital))
                    else:
                        continue
    return maxNum





print(pandigitalMultiples(9))