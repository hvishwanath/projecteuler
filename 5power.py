def fib(n):
    if n==1:
        return 1
    if n==2:
        return 2
    return fib(n-1) + fib(n-2)

def fifthPower(number):
    sum = 0
    cp = number
    while number!=0:
        rem = number % 10
        number = number / 10
        sum = sum + pow(rem,5)
    if sum == cp:
        return True
    return False

factorialDict = {
    0:1,
    1:1,
    2:2,
    3:6,
    4:24,
    5:120,
    6:720,
    7:5040,
    8:40320,
    9:362880
    }
def isCuriousNumber(n):
    cp = n
    sum = 0
    global factorialDict
    while n!=0:
        rem = n%10
        n = n/10
        sum = sum + factorialDict[rem]
        
    if sum == cp:
        return True
    return False

def main():
    li = []
##    for i in range(100,10000000):
##        if fifthPower(i):
##            li.append(i)

    for i in range(10,10000000):
        if isCuriousNumber(i):
            li.append(i)

    print "Range 100-100000, Curious Numbers : %s" % repr(li)
    #Range 100-100000, Number of 5th Powers : [4150, 4151, 54748, 92727, 93084, 194979]
    

if "__main__" == __name__:
    main()
##    li = [4150, 4151, 54748, 92727, 93084, 194979]
##    s = 0
##    for n in li:
##        s = s + n
    #print "Sum : %d" % s