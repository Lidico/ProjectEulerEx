import math

from pip._vendor.urllib3.connectionpool import xrange


def isPrime(num):
    prime = True
    if num < 2: return False
    if num == 2: return True
    for factor in range(3,int(math.sqrt(num)),2):
        if num % factor == 0: prime = False
    return prime

def howManyPrimes(a, b):
    n = 0
    while True:
        if isPrime(n**2 + n*a + b):
            n += 1
        else:
            break
    return n

def quadraticPrimes(limitNum):
    bestValue = (-limitNum*2,-limitNum*2,0)
    for a in xrange(-limitNum, limitNum+1):
        for b in xrange(-limitNum, limitNum+1):
            n = howManyPrimes(a, b)
            if n > bestValue[2]:
                bestValue = (a, b, n)
    return bestValue

x = quadraticPrimes(1000)
print('the best a is: ', x[0], 'and best b is: ', x[1] , 'with ',x[2], ' primes')


