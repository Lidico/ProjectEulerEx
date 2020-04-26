"""
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.
Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
(Please note that the palindromic number, in either base, may not include leading zeros.)
"""
from pip._vendor.urllib3.connectionpool import xrange

def reverse(num):
    return num[::-1]

def isPalindrome(num):
    rev = reverse(num)
    if (num == rev):
        return True
    return False

def doubleBasePalindromes(n):
    sumOfPal = 0
    for num in xrange(11,n):
        binary = bin(num)[2:]
        if str(num)[0] == str(num)[len(str(num))-1] and str(binary)[0] == str(binary)[len(str(binary))-1]:
            if isPalindrome(str(num)) and isPalindrome(str(binary)):
                sumOfPal += num
        else:
            continue
    return sumOfPal


print(doubleBasePalindromes(1000000))
