def divide(num, den, limit):
    l = []
    digits = 0
    pointInQuotient = False
    
    divisor = den
    dividend = num

    while (digits < limit) and (dividend != 0):
        pointMultiplied = False
        while dividend < divisor :
            if pointInQuotient and (not pointMultiplied):
                pointMultiplied = True
                dividend = dividend * 10
                continue
            if not pointInQuotient:
                pointInQuotient = True
                l.append('.')
                dividend = dividend * 10
                continue
            l.append('0')       #Append a zero otherwise
            dividend = dividend * 10
            digits = digits + 1
            
        # Ready for division now.
        quotient = dividend / divisor
        remainder = dividend % divisor
        l.append(str(quotient))
        dividend = remainder
        digits = digits + 1
        #print l, dividend, divisor
    return l

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

if __name__ == "__main__":
    num = 1
    d = 2
    for i in range(2,1000):
        s = ''.join(divide(num,i,200))
        print num, '/', i, " = " ,s, " = ", findRecurringSubstring(s.replace('.',''))
            
                
                
            
