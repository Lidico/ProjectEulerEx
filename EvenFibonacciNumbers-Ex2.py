def evenFibonacciNumbers():
    FOURMILLION = 4000000

    #The inition of the Fibonacci List is 1 and 2
    listOfFibonacci =[1,2]
    count = 1
    while listOfFibonacci[count-1]+listOfFibonacci[count] < FOURMILLION:
        #Appending the sum of two last numbers
        listOfFibonacci.append(listOfFibonacci[count-1]+listOfFibonacci[count])
        count+=1
    return listOfFibonacci

print(evenFibonacciNumbers())