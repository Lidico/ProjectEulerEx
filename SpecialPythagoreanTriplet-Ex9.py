#A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#a2 + b2 = c2
#For example, 32 + 42 = 9 + 16 = 25 = 52.
#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.

def specialPythagoreanTriplet(n):
    #(ak)^2+(bk)^2=(ck)^2
    #Lets use Clasic a=3 b=4 c=5
    #3+4+5 = 12
    SUMOFCLASSICS = 12
    k = n/SUMOFCLASSICS
    return (round(3*k),round(4*k),round(5*k))

print(specialPythagoreanTriplet(1000))
