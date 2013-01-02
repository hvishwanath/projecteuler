# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="HVISHWANATH"
__date__ ="$Aug 10, 2010 3:53:59 PM$"


def splitFraction(e):
    x = e.split('/')
    if len(x) == 1:
        return x[0],1
    else:
        return x[0],x[1]

def fractionAdd(expr):
    #Right now can parse only two expressions.Therfore one Operator
    if expr.count('+') > 1:
        raise exceptions.NotImplementedError("Cannot parse expressions with more than 2 terms!")
    (term1,term2) = expr.split('+')
    nm1,dn1 = splitFraction(term1)
    nm2,dn2 = splitFraction(term2)

    nm1 = int(nm1)
    dn1 = int(dn1)
    nm2 = int(nm2)
    dn2 = int(dn2)

    if dn1 != dn2:
        #Find LCM
        lcm = getLCM(dn1,dn2)
        nm1 = nm1 * (lcm/dn1)
        nm2 = nm2 * (lcm/dn2)
        dn1 = lcm

    return nm1+nm2,dn1

def getLCM(n1,n2):
    """getLCM(n1,n2) => LCM of n1, n2"""
    pfn1 = primeFactorize(n1)
    pfn2 = primeFactorize(n2)

    distinctPrimes = []
    for item in pfn1:
        if item in distinctPrimes:
            continue
        distinctPrimes.append(item)

    for item in pfn2:
        if item in distinctPrimes:
            continue
        distinctPrimes.append(item)

    lcmdict = {}
    for item in distinctPrimes:
        lcmdict[item] = max([listCount(pfn1,item),listCount(pfn2,item)])

    lcm = 1
    for key in lcmdict.keys():
        lcm = lcm * (key ** lcmdict[key])

    return lcm

def listCount(li,n):
    cnt = 0
    for item in li:
        if item == n:
            cnt = cnt + 1
    return cnt

def primeFactorize(n):
    """primeFactorize(n) => List of Prime Factors of n"""

    if isPrime(n):
        return [n]

    p = 1
    pf = []
    x = n
    while p!=x:
        if isPrime(n):
            pf.append(n)
        elif n%2 == 0:
            pf.append(2)
            n = n/2
        elif n%3 == 0:
            pf.append(3)
            n = n/3
        elif n%5 == 0:
            pf.append(3)
            n = n/5
        elif n%7 == 0:
            pf.append(3)
            n = n/7
        p = 1
        for item in pf:
            p = item*p
    return pf


def reverse(n):
    """reverse(n) => reverses n and returns
    n is of type string
    """
    x = list(n)
    x.reverse()
    return ''.join(x)

def ncr(n,r):
    """ncr = n!/(r!*(n-r)!)"""
    nfact = factorialNonRecursive(n)
    rfact = factorialNonRecursive(r)
    nminusr = factorialNonRecursive(n-r)
    return (nfact /(rfact * nminusr))

def factorialNonRecursive(n):
    if n==0: return 1
    p = 1
    for i in range(1,n+1):
        p = p * i
    return p

def repeats(number):
    """repeats(number) => Dict {repeating number : no. of times}"""
    d = {}
    x = str(number)
    for c in x:
        a = x.count(c)
        if a>1:
            d[int(c)] = a
    return d


def permute(s):
    """Permute(str/int) -> Returns a sorted list of possible Perumutations"""
    import types
    if type(s) == types.IntType:
        s = str(s)
    x = []
    a = list(s)
    n = len(a)
    #Create p
    p = []
    for i in range(0,n):
        p.append(0)
    i = 1
    while (i<n):
        if p[i] < i:
            j = 0
            if i%2 !=0 : j=p[i]
            temp = a[j]
            a[j] = a[i]
            a[i] = temp
            p[i] = p[i] + 1
            i = 1
        else:
            p[i] = 0
            i = i+1
        b = ''.join(a)
        if b not in x: x.append(b)
    x.append(s)
    x.sort()
    return x


def getPentagonalNumbers(nterm,startterm=1):
    """
    getPentagonalNumbers(int nterm)
    => P_(n)=n(3n-1)/2 List upto nterm
    """
    cntr = startterm
    li = []
    while cntr <= nterm:
        li.append((cntr * ((3*cntr)-1))/2)
        cntr = cntr + 1
    return li


def getTriangularNumbers(nterm):
    """
    getTriangularNumbers(int nterm<inclusive>)
    Returns list of Triangular Numbers till nterms.
    Triangular Numbers-> T7 = 1+2+3+4+5+6+7
    """
    li = []
    for i in range(1,nterm+1):
        li.append((i*(i+1))/2)
    return li

def isPrime(number):
    """isPrime(number)
    Returns True if Prime, False otherwise
    """
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
    """isPandigital(int number).
    If all digits are used only once in the number, returns True
    Returns False otherwise.
    """

    sn = str(number)
    for c in sn:
        if sn.count(c) > 1:
            return False
    return True

def getDivisors(i):
    """
    getDivisors(int i)
    Returns a list of divisors for the number.
    """
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
    """
    getListSum(list li)
    Takes a integer/float list, Returns the sum of all elements in it
    """
    sum = 0
    for x in l:
        sum = sum+x
    return sum

def to_base(number,basek):
    """
    to_base(number, base)
    Converts the given number to passed base.
    Both number and base should be integers, base (2-10 inclusive)
    """

    ret_value=""
    sign=""
    if number < 0:
        sign="-"
        number = -number
    if number == 0:
        return  "0"
    while number>0:
        digit = number % basek
        number = number / basek
        ret_value = str(digit) + ret_value
    return int(sign+ret_value)

def rotate(current,original):
    """
    rotate(current state, original number)
    Both are integers. Returns a rotated version if possible.
    Else returns -1.
    """
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

def getPrimeList(ll,ul):
    """getPrimeList(lowerlimit, upperlimit <exclusive>)
    Returns a list of Prime numbers between the limits
    """
    primeList = []
    for i in range(ll,ul):
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

def isListEntirelyPrime(li):
    """isListEntirelyPrime(li)
    Returns True if all numbers in the list is Prime.
    False otherwise
    """
    for n in li:
        if not isPrime(int(n)):
            return False
    return True

def getPythogoreanTriplets(limit):
    """getPythogoreanTriplets(limit) => Dict of Pythogorean triplets"""
    d = {}

    for i in range(1,limit+1):
        for j in range(1,limit+1):
            x = sqrt(((i*i) + (j*j)))
            if int(x) == x: #Perfect Sqare
                x = int(x)
                perimeter = x + i + j
                if perimeter > 1000:
                    continue
                templist = [x,i,j]
                if d.has_key(perimeter):
                    d[perimeter].append(templist)
                else:
                    d[perimeter] = []
                    d[perimeter].append(templist)
    return d

def getBidirectionalTrucatedList(number):
    """getBidirectionalTruncatedList(int number)
    Returns possible truncations from both directions
    """
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

def fib(n):
    """
    fib(which term?)
    Returns fibonacci number corresponding to n
    Uses Recursion
    """
    if n==1:
        return 1
    if n==2:
        return 2
    return fib(n-1) + fib(n-2)

def findRecurringSubstring(s):
    """ Find the recurring substring in a given string """
    x = {}
    for c in s:
        cnt = s.count(c)
        if cnt != 1:
            if x.has_key(cnt) :
                if x[cnt].count(c) == 0:
                    x[cnt].append(c)
            else : x[cnt] = [c]
    l = [(len(z), z )for z in x.values()]
    l.sort()
    retStr = ""
    try:
        retStr = "%s :: %s" % (l[-1], l[-2])
    except:
        pass

    return retStr

def isPalindrome(number):
    n = str(number)
    cp = list(n)
    li = list(n)
    li.reverse()
    return cp == li

def isLeapYear(year):
    leap = False
    if year%100 == 0:
        if year%400 == 0:
            leap = True
    elif year%4 == 0:
        leap = True
    return leap

def getNumberOfLeapYears(syear,eyear,):
    #Returns number of leap years between start year and end year
    cntr = 0
    for i in range(syear,eyear):
        if isLeapYear(i):
            cntr = cntr + 1
    return cntr

def isPrime(number):
    prime = True
    x = 2
    while x*x <= number:
        if number % x == 0:
            prime = False
            break
        x = x + 1
    return prime

def nprString(s,r):
    """ s : String to be permutated.
        r : Number of characters in the string to be taken at a time.
        returns : list of possible permutations. Uses nPr = n! / (n-r)!
    """

    if r == 1:
        rl = []
        for c in s:
            rl.append(c)
        return rl

    rl = []
    for i in range(0,len(s)):
        # @type s str
        x = nprString(s.replace(s[i],''),r-1)
        #x = nprString(s,r-1)
        for item in x:
            rl.append(list(s[i]) + list(item))

    return rl

def cube_root(n):
    "A modified Newton's Method solver for integral cube roots."
    if int(n) != n:
        raise ValueError("must provide an integer")
    if n in (-1,0,1): return n
    offset = (1,-1)[n > 0]
    x = n/2
    seen = set()
    steps = 0
    while 1:
        y = x**3
        if y == n:
            #~ print "Found %d ^ 1/3 = %d in %d steps" % (n,x,steps)
            return x
        dydx = 3.0*x*x
        x += int((n-y)/dydx)+offset
        x = x or 1
        if x in seen:
            raise ValueError("%d is not a perfect cube" % n)
        seen.add(x)
        steps += 1

if __name__ == "__main__":
    print "Hello World"
