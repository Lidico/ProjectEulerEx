"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example,
 the 5-digit number, 15234, is 1 through 5 pandigital.
The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier,
 and product is 1 through 9 pandigital.
Find the sum of all products whose multiplicand/multiplier/product
identity can be written as a 1 through 9 pandigital.
HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
"""
from pip._vendor.urllib3.connectionpool import xrange

def soretedString(string):
    digits = str(string)
    digits = ''.join(sorted(digits))
    return digits

def containsZeros(num):
    digits = str(num)
    digits = ''.join(sorted(digits))
    if digits[0] == '0':
        return True
    else:
        return False

def checkRepeatNumber(num):
    digits = str(num)
    if len(digits) == len(set(digits)):
        return False
    else:
        return True

def sameDigits(num1, num2):
    a = str(num1)
    b = str(num2)
    a_set = set(a)
    b_set = set(b)
    if (a_set & b_set):
        return True
    else:
        return False

def pandigitalProducts(n):
    digits = []
    listOfPrud = []
    for i in xrange(1,n+1):
        digits.append(str(i))
    for mulp1 in xrange(2,98):
        for mulp2 in xrange(2,9876):
            if containsZeros(mulp1) or containsZeros(mulp2):
                continue
            if checkRepeatNumber(mulp1) or checkRepeatNumber(mulp2):
                continue
            if sameDigits(mulp1, mulp2):
                continue
            tempDigits = digits.copy()
            tempDigits = list(set(tempDigits)-set(str(mulp1)))
            tempDigits = list(set(tempDigits) - set(str(mulp2)))
            strTempDigits = ''.join(tempDigits)
            if soretedString(strTempDigits) == soretedString(str(mulp1*mulp2)):
                listOfPrud.append(mulp1)
                listOfPrud.append(mulp2)
                listOfPrud.append(mulp1*mulp2)
    listOfPrud = list(dict.fromkeys(listOfPrud))
    return sum(listOfPrud)



    return digits

print(pandigitalProducts(9))