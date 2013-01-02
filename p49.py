from utils import *

def arePermutations(number,fn,sn):
    x = str(number)
    y = str(fn)
    z = str(sn)
    l = list(x)

    for c in y:
        if c not in l:
            return False
    for c in z:
        if c not in l:
            return False
    return True

def main():
    #Get Primes from 1000-10000
    li = getPrimeList(1000,10000)
    #Detect arithmetic series. The common difference can range
    #from 1-9999. Try to detect T3.
    #Tn = a+(n-1)d
    for item in li:
        for d in range(1,10000):
            t3 = item + (2*d)
            t2 = item + d
            if t2 in li and t3 in li:
                #See if they are permutations.
                if arePermutations(item,t2,t3):
                    print item,t2,t3,d

if __name__ == "__main__":
    main()