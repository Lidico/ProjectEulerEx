import math

def largerPrimeFactor(number):
    maxPrime = 0

    #Handle the case number is Even
    while number % 2 == 0:
        maxPrime = 2
        number /= 2

    #Skips the even numbers
    for i in range(3, int(math.sqrt(number)) + 1, 2):
        while number % i == 0:
            maxPrime = i
            number = number / i
    # This condition is to handle the case when n is a prime number greater than 2
    if number > 2:
        maxPrime = number

    return int(maxPrime)

print(largerPrimeFactor(600851475143))