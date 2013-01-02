def listMerge(l1, l2):
    r = []
    for item in l2:
        #print item
        x = []
        x.extend(l1)
        try:
            x.extend(item)
        except:
            x.extend([item])
        r.append(x)
    return r

def findCombinations(numset, target):
    if target == 0:
        return [0]
    
    numset.sort()
    retList = []
    if len(numset) == 1 and numset[0] == 1:     #Forming target with only 1s
        return [target]
    
    #Otherwise, find the no.of times the bigger number can be multiplied.
    bigNum = numset[-1]
    divisor = target / bigNum
    noOfTimes = [divisor]

    numset.remove(bigNum)
    noOfTimes.extend(findCombinations([x for x in numset], target % bigNum))
    #retList.append(listMerge(noOfTimes, findCombinations([x for x in numset], target % bigNum)))

    retList.append(noOfTimes)
    
    while divisor != 0:
        divisor = divisor - 1;
        noOfTimes = [divisor]

        noOfTimes.extend(findCombinations([x for x in numset], target - (bigNum * divisor)))
        #retList.append(listMerge(noOfTimes, findCombinations([x for x in numset], target - (bigNum * divisor))))

        retList.append(noOfTimes)

    return retList

if __name__ == "__main__":
    print "\n".join([str(x) for x in findCombinations([10,5,2,1],16)])
        