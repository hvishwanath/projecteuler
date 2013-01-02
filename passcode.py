import os,sys

def whatAnIdeaSirJee(li,prevEle,curEle,nextEle):
    #The procedure as below :
    #1. If Ele is found :
    #       Check if Pred <- Ele -> Succ is in Order in the list. If not adjust
    #2. If Ele is not found :
    #       If Pred is not None, insert it just after pred if Pred in List
    #       Else if Pred is None and Succ is Not None, insert it just before Succ if Succ in List
    #       If Neither Pred nor Succ in List, Append it to the end of List.
    if curEle in li:
        ci = li.index(curEle)
        if prevEle in li:
            pi = li.index(prevEle)
            if not pi < ci:
                del li[pi]  #Delete
                #Recalculate
                ci = li.index(curEle)
                li.insert(ci,prevEle)
        elif prevEle and (prevEle not in li):
            li.insert(ci,prevEle)
        if nextEle in li:
            ni = li.index(nextEle)
            if not ni > ci:
                del li[ni]
                ci = li.index(curEle)
                li.insert(ci+1,nextEle)
        elif nextEle and (nextEle not in li):
            li.insert(ci+1,nextEle)
    elif curEle not in li:
        if prevEle and (prevEle in li):
            li.insert(li.index(prevEle)+1,curEle)
        elif nextEle and (nextEle in li):
            li.insert(li.index(nextEle),curEle)
        else:
            li.append(curEle)
    return li
        
    
def main():
    f = sys.argv[1] #Filename    
    numberList = file(f).read().split('\n')
    print "Created numberList of length : %s" % repr(len(numberList))
    li = []
    for n in numberList:
        #First sequence is a List
        if li == []:
            li = list(n)
        #After this, each key element is inserted into the list created above.
        #Every digit in the key element carrys 2 pieces of info, Pred <- Ele -> Succ
        else:
            prevEle = None
            nextEle = None
            for i in range(0,len(n)):
                curEle = n[i]
                if i == 0:
                    prevEle = None
                else:
                    prevEle = n[i-1]
                if i == len(n)-1:
                    nextEle = None
                else:
                    nextEle = n[i+1]
                li = whatAnIdeaSirJee(li,prevEle,curEle,nextEle)
        #print "Current Key Element : %s\nCurrent List Status : %s\n\n" % (repr(n),repr(li))
    print "Cracked Passcode is : %s" % repr(li)
    return

if "__main__" == __name__:
    main()