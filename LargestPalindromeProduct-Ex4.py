
def largerPalindromProduct(n):
    numbers = [pow(10,n)-1, pow(10,n)-1]
    count = 0
    for i in range(numbers[0], 0, -1):
        count += 1
        if count == 100:
            numbers[0] = pow(10,n)-1
            numbers[1] -= 1
            count = 0
        res = str(numbers[0]*numbers[1]) == str(numbers[0]*numbers[1])[::-1]
        if res:

            return numbers
        else:
            numbers[0] -= 1



twoLargerNums = largerPalindromProduct(3)
print(twoLargerNums[0], "*", twoLargerNums[1], "=", twoLargerNums[0]*twoLargerNums[1])