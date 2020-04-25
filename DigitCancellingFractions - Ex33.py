"""
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may
 incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.
We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two
digits in the numerator and denominator.
If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
"""
from pip._vendor.urllib3.connectionpool import xrange

def isCuriousFraction(x, y):

    if set(str(x)) & set(str(y)) == set():
        return 1
    if set(str(x)) & set(str(y)) == {'0'}:
        return 1
    a = list(set(str(x)).difference(str(y)))
    b = list(set(str(y)).difference(str(x)))

    if a == [] or b == [] or int(b[0]) == 0:
        return 1
    if int(a[0])/int(b[0]) == x/y:
        return int(b[0])
    else:
        return 1


def digitCancellingFractions():
    count = 0
    prodOfDenominator = 1
    for x in xrange(11,100):
        for y in xrange(11,100):
            if count == 4:
                break
            if isCuriousFraction(x,y) != 1:
                count += 1
                prodOfDenominator *= isCuriousFraction(x,y)
    return prodOfDenominator

print(digitCancellingFractions())
