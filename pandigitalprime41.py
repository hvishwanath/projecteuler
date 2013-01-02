def isPrime(number):
    if number == 1:
        return False
    prime = True
    x = 2
    while x*x <= number:
        if number % x == 0:
            prime = False
            break
        x = x+1
    return prime

def isPandigital(number):
    sn = str(number)
    for c in sn:
        if sn.count(c) > 1:
            return False
    return True
    
def largestPandigitalPrime(number,incr=True):
    #Largest should be having 1,2,3,4,5,6,7,8,9 and 0 only once
    i = number

    while True:
        print i
        if isPandigital(i) and isPrime(i):
            print "Largest Pandigital Prime : %d" % i
            break
        if incr:
            i = i+1
        else:
            i = i-1

if __name__ == "__main__":
    largestPandigitalPrime(987654103+1)