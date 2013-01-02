from math import *

def getSumOfDigits(num):
    x = str(num)
    sum = 0
    for c in x:
        sum = sum + int(c)

    return sum

maxdigitalsum = 0
for i in range(1,100):
    for j in range(1,100):
        s = int(i**j)
        t = getSumOfDigits(s)
        if maxdigitalsum < t:
            maxdigitalsum = t

print "Max Digital Sum : %d" % maxdigitalsum            