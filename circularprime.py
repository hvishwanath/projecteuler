import string

def rotate(current,original):
    #Receives a number
    x = list(str(current))
    y = []
    y.extend(x)
    temp = ''
    l = len(x)
    for i in range(0,l):
        if i < (l-1):
            y[i+1] = x[i]
        elif i == (l-1):
            y[0] = x[i]
    
    temp = int(string.join(y,''))
    
    if temp==original:
        return -1
    elif len(str(temp)) != len(str(original)):
        return -1
    return temp

def isPrime(number):
    prime = True
    x = 2
    while x*x <= number:
        if number % x == 0:
            prime = False
            break
        x = x + 1
    return prime

def getPrimeList(limit):
    primeList = []
    for i in range(100,limit):
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

def main():
    print "Getting Prime Numbers List 100 - 1 Million..."
    primeList = getPrimeList(1000000)
    print "Total Primes 100 - 1 Million : %d" % len(primeList)
    circularPrimeList = []
    print "Determining Circular Primes..."
    for number in primeList:
        #Find all possible rotations
        print number
        rotationList = []
        original = cur = number        
        cur = rotate(cur,original)
        while cur!=-1:  #End of possible rotations        
            rotationList.append(cur)
            cur = rotate(cur,original)
        #Determine if the number is a circular Prime
        #For each possible rotation in rotationList,
        #Check if the number is Prime.
        cp = True
        for rot in rotationList:
            if rot not in primeList:
                cp = False
                break
        if cp:
            primeList.remove(number)
            circularPrimeList.append(number)
            circularPrimeList.extend(rotationList)
            for rot in rotationList:
                primeList.remove(rot)
        
    print "Total Number of Circular Primes : %d" % len(circularPrimeList)
    
if "__main__" == __name__:
    main()
        