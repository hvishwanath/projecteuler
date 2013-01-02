from utils import *
from math import *

sum = 0
cntr = 2
diagElements = [1]

def getPrimeCount(l):
    cnt = 0
    for ele in l:
        if isPrime(ele):
            cnt = cnt + 1
    return cnt

i = 3
while True:
    #calc the Top right diag ele
    tr = i*i
    #get the remaining three
    a = tr-cntr
    b = a-cntr
    c = b-cntr
    cntr = cntr + 2 #Increment counter by 2
    #Add them to diag elements
    diagElements.extend([a,b,c,tr])
    cnt = getPrimeCount(diagElements)
    ratio = round(float(cnt)/len(diagElements),2)
    if ratio < 0.10:
        print i
        break
    i = i+2

