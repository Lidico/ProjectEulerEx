def specialPythagoreanTriplet(n):
    import math
    #(ak)^2+(bk)^2=(ck)^2
    #Lets use Clasic a=3 b=4 c=5
    #3+4+5 = 12
    SUMOFCLASSICS = 12
    k = n/SUMOFCLASSICS
    return (round(3*k),round(4*k),round(5*k))

print(specialPythagoreanTriplet(1000))
