from types import IntType
from math import sqrt

def getPythogoreanTriplets(limit):
    d = {}
    
    for i in range(1,limit+1):
        for j in range(1,limit+1):
            x = sqrt(((i*i) + (j*j)))
            if int(x) == x: #Perfect Sqare
                x = int(x)
                perimeter = x + i + j
                if perimeter > 1000:
                    continue
                templist = [x,i,j]                
                if d.has_key(perimeter):
                    d[perimeter].append(templist)
                else:
                    d[perimeter] = []
                    d[perimeter].append(templist)
    return d

#For p=840, There are 16 possible solutions. This is the max.
                