# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="HVISHWANATH"
__date__ ="$Aug 10, 2010 4:12:08 PM$"

from generalutils import getDivisors
import generalutils

LIMIT = 28123

def isAbundantNumber(i):
    divisorList = getDivisors(i);
    if i in divisorList:
        divisorList.remove(i)
    sum = 0
    for x in divisorList:
        sum = sum + x
    if sum > i:
        #print "%d : [%s], Sum : %s" % (i,divisorList,sum)
        return True
    return False

def getAbundantNumbers(limit):
    abundantNumberList = []
    for i in range(12,limit):
        if isAbundantNumber(i):
            abundantNumberList.append(i)
    return abundantNumberList


def main():
    al = getAbundantNumbers(LIMIT)
    print len(al)
    sum = 0
    for i in al:
        sum = sum + i

    print "Sum of Abundant Numbers : ", sum

#if __name__ == "__main__":
#    main()
