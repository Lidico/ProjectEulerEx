#The sum of the squares of the first ten natural numbers is,
#12+22+...+102=385
#The square of the sum of the first ten natural numbers is,
#Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025−385=2640
#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.


def sumSquareDifference(n):

    sumSquares = 0
    sumToSquare = 0
    for i in range(0, n+1):
        sumSquares += i**2
        sumToSquare += i
    return sumToSquare**2-sumSquares

print(sumSquareDifference(100))
