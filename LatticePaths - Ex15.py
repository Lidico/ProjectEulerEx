"""
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down,
 there are exactly 6 routes to the bottom right corner.
How many such routes are there through a 20×20 grid?
"""
import math

def latticePaths(n):
    """
    if 1 in right and 0 is down
    to get to the bottom right corner i have to move right (1) 20 times and down(0) 20 times
    i use the Combinatorics way
        you need to set 1111111111111111111100000000000000000000 in every possible way
    the furmula is simple 2*((2n-1)! above n) or 2*((2n-1)!/(n-1)!*n!)
    """
    return 2*int(math.factorial(n+n-1)/(math.factorial(n-1)*math.factorial(n)))

print(latticePaths(20))