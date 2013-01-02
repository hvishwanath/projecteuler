from utils import *

maxLimit = 10000
maxiter = 50
nonLychrelcntr = 0
lychrelcntr = 0

for i in range(1,maxLimit):
    lychrel = True
    temp = i
    noOfIter = 0
    for j in range(0,maxiter):
        noOfIter = noOfIter + 1
        a = int(reverse(str(temp)))
        s = a + temp
        if isPalindrome(s):
            lychrel = False
            nonLychrelcntr = nonLychrelcntr+1
            #print i, s, noOfIter
            break
        temp = s
    if lychrel : lychrelcntr = lychrelcntr + 1

print "Total Number of Non Lychrel Numbers below %d : %d" % (maxLimit,nonLychrelcntr)
print "Total Number of Lychrel Numbers below %d : %d" % (maxLimit,lychrelcntr)