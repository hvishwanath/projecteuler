def containsSameDigits(origNumber,newNumber):
    l = list(str(origNumber))
    m = []
    m.extend(l)
    x = str(newNumber)
    if len(x) != len(l):
        return False
    
    for c in x:
        if c in l:
            l.remove(c)
        elif c not in l:
            return False
    return True

def solvep52():
    i = 10
    while True:
        if containsSameDigits(i,2*i) and \
           containsSameDigits(i,3*i) and \
           containsSameDigits(i,4*i) and \
           containsSameDigits(i,5*i) and \
           containsSameDigits(i,6*i):
            print i
            break
        i = i + 1

if "__main__" == __name__:
    solvep52()