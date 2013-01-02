def getPrimeList(ll,ul):
    primeList = []
    for i in range(ll,up):
        x = 2
        prime = True
        while x*x <= i:
            if i%x == 0:
                prime = False
                break
            x = x+1
        if prime:
            primeList.append(i)
    return primeList

def isPrime(number):
    if number == 1:
        return False
    prime = True
    x = 2
    while x*x <= number:
        if number % x == 0:
            prime = False
            break
        x = x + 1
    return prime

def isListEntirelyPrime(li):    
    for n in li:
        if not isPrime(int(n)):
            return False
    return True

def getBidirectionalTrucatedList(number):
    sn = str(number)
    wcopy = sn
    tlist = []
    #Left 2 Right
    for i in range(-len(sn)+1,0):
        tlist.append(sn[i:])

    #Right 2 Left
    i = -1
    while i != -len(sn):
        tlist.append(sn[:i])
        i = i-1
    return tlist

def main():
    cntr = 0
    interstingPrimes = []
    i = 11
    while True:
        if isPrime(i):
            l = getBidirectionalTrucatedList(i)
            if isListEntirelyPrime(l):
                cntr = cntr + 1
                interstingPrimes.append(i)
                #print "Adding %d to InterstingPrimes" % i
                #print "Biderctional Trucated List for %d is : %s" % (i,repr(l))
                if cntr == 11:
                    break
        i = i+1
    print "List of Intersting Primes : %s" % repr(interstingPrimes)
    s = 0
    for n in interstingPrimes:
        s = s + n
    print "Their Sum : %d" % s

if __name__ == "__main__":
    main()
        
    