"""
By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

       3
      7 4
     2 4 6
    8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

                           75
                          95 64
                         17 47 82
                        18 35 87 10
                       20 04 82 47 65
                      19 01 23 75 03 34
                     88 02 77 73 07 63 67
                    99 65 04 28 06 16 70 92
                  41 41 26 56 83 40 80 70 33
                 41 48 72 33 47 32 37 16 94 29
                53 71 44 65 25 43 91 52 97 51 14
               70 11 33 28 77 73 17 78 39 68 17 57
              91 71 52 38 17 14 91 43 58 50 27 29 48
             63 66 04 68 89 53 67 30 73 16 69 87 40 31
           04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route. However, Problem 67, is the same challenge with a triangle containing one-hundred rows; it cannot be solved by brute force, and requires a clever method! ;o)
"""

def maximumPathSumI(triMat):
    if len(triMatrix) != len(triMatrix[0]): return -1
    isEnd = False
    greatesSum = triMat[0][0]
    i, j = 0, 0
    while isEnd != True:
        if triMat[i][j+1] == 0 or triMat[i + 1][j] == 0:
            isEnd = True
        if triMatrix[i+1][j] >= triMatrix[i][j + 1]:
            greatesSum += triMatrix[i + 1][j]
            i += 1
        else:
            greatesSum += triMatrix[i][j + 1]
            j += 1
    return greatesSum

triMatrix = [[75,64,82,10,65,34,67,92,33,29,14,57,48,31,23],
             [95,47,87,47,3,63,70,70,94,51,17,29,40,4,0],
             [17,35,82,75,7,16,80,16,97,68,27,87,60,0,0],
             [18,4,23,73,6,40,37,52,39,50,69,53,0,0,0],
             [20,1,77,28,83,32,91,78,58,16,38,0,0,0,0],
             [19,2,4,56,47,43,17,43,73,93,0,0,0,0,0],
             [88,65,26,33,25,73,91,30,73,0,0,0,0,0,0],
             [99,41,72,65,77,14,67,98,0,0,0,0,0,0,0],
             [41,48,44,28,17,53,70,0,0,0,0,0,0,0,0],
             [41,71,33,38,89,9,0,0,0,0,0,0,0,0,0],
             [53,11,52,68,23,0,0,0,0,0,0,0,0,0,0],
             [70,71,4,27,0,0,0,0,0,0,0,0,0,0,0],
             [91,66,98,0,0,0,0,0,0,0,0,0,0,0,0],
             [63,62.0,0,0,0,0,0,0,0,0,0,0,0,0,0],
             [4,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

print(maximumPathSumI(triMatrix))