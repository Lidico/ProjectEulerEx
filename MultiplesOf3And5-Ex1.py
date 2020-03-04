#If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.

def multiplyOf3and5():
    sumOf5 = 0
    sumOf3 = 0
    sumOf15 = 0
    k = 0

    #Connecting all multiples of 3
    while k <=999:
        sumOf3 += k
        k += 3
    k = 0

    # Connecting all multiples of 5
    while k <=995 :
        sumOf5 += k
        k += 5
    k = 0

    # Connecting all multiples of 15(5*3)
    while k <= 990:
        sumOf15 += k
        k += 15
    return sumOf3+sumOf5-sumOf15

print(multiplyOf3and5())


