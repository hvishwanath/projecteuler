def getDivisors(i):
    divlist = []
    x = 1
    while x*x <= i:
        if i%x == 0:
            divlist.append(x)
            divlist.append(i/x)
        x = x+1
    divlist.sort()
    return divlist

def getListSum(l):
    sum = 0
    for x in l:
        sum = sum+x
    return sum

def main():
    amicableNumbers = []
    for i in range(2,10000):
        if i in amicableNumbers:
            continue
        dlist = getDivisors(i)
        dlist.remove(i)
        dOfi = getListSum(dlist)
        slist = getDivisors(dOfi)
        slist.remove(dOfi)
        if getListSum(slist) == i:
            if not i==dOfi:
                amicableNumbers.append(i)
                amicableNumbers.append(dOfi)
    print "List of all Amicable Numbers : " + str(amicableNumbers)
    print "Sum of all Amicable Numbers below 10000 : %d" % getListSum(amicableNumbers)
    return
        
if __name__ ==  "__main__":
    main()
    