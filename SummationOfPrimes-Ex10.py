
def isPrime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def summationOfPrimes(n):
    primeNum = 3
    sumOfPrimesBelow = 2
    while primeNum < n:
        if isPrime(primeNum):
            sumOfPrimesBelow += primeNum
        primeNum += 2
    return sumOfPrimesBelow

print(summationOfPrimes(2000000))