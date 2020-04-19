"""
In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?
"""
from pip._vendor.urllib3.connectionpool import xrange

def coinSums(n):
    if n > 10 or n<1: return 0
    coins = {1: 1, 2: 2, 3: 5, 4: 10, 5: 20, 6: 50, 7: 100, 8: 200}
    pound = n * 100
    numOfWays = [1] + [0]*pound
    for coin in coins.values():
        for i in xrange(coin, pound + 1):
            numOfWays[i] += numOfWays[i - coin]
    return numOfWays[pound]

print(coinSums(2))

