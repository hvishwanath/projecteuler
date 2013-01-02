"""
Let D_(0) be the two-letter string "Fa". For n?1, derive D_(n) from D_(n-1) by the string-rewriting rules:

"a" -> "aRbFR"
"b" -> "LFaLb"

Thus, D_(0) = "Fa", D_(1) = "FaRbFR", D_(2) = "FaRbFRRLFaLbFR", and so on.

These strings can be interpreted as instructions to a computer graphics program, with
"F" meaning "draw forward one unit",
"L" meaning "turn left 90 degrees",
"R" meaning "turn right 90 degrees",
and "a" and "b" being ignored.
The initial position of the computer cursor is (0,0), pointing up towards (0,1).
"""

d = {
    'a':'aRbFR',
    'b':'LFaLb'
    }

def getDDn(n):
    D0 = "Fa"
    if n==0:
        return D0
    Dprev = D0
    for i in range(1,n+1):
        print "Creating D%d" %i
        Dn = ''
        getaindex = True
        getbindex = True
        aprevindex = 0
        bprevindex = 0
        copyindex = 0
            
        while True:
            if getaindex :
                try:
                    aindex = Dprev.index('a',aprevindex)            
                except:
                    aindex = -1
                    getaindex = False
            if getbindex:
                try:
                    bindex = Dprev.index('b',bprevindex)                    
                except:
                    bindex = -1
                    getbindex = False

            if aindex != -1 and bindex != -1: #When both literals are still present
                mindex = min([aindex,bindex])
                if mindex == aindex:                    
                    Dn = Dn + Dprev[copyindex:aindex]
                    Dn = Dn + d['a']
                    aprevindex = aindex + 1
                    copyindex = aindex + 1
                elif mindex == bindex:
                    Dn = Dn + Dprev[copyindex:bindex]
                    Dn = Dn + d['b']
                    bprevindex = bindex + 1
                    copyindex = bindex + 1
            elif aindex==-1 and bindex==-1:
                try:
                    Dn = Dn+Dprev[copyindex:]
                except:
                    pass
                break
            else:
                if aindex != -1:
                    Dn = Dn + Dprev[copyindex:aindex]
                    Dn = Dn + d['a']
                    copyindex = aindex + 1
                    aprevindex = aindex + 1                    
                elif bindex != -1:
                    Dn = Dn + Dprev[copyindex:bindex]
                    Dn = Dn + d['b']
                    bprevindex = bindex + 1
                    copyindex = bindex + 1
        Dprev = Dn
        print "Total Length of D%d : %d" %(i,len(Dn))
    return Dn


def getDn(n):
    D0 = "Fa"
    if n==0:
        return D0
    Dprev = D0
    for i in range(1,n+1):
        print "Creating D%d" %i
        Dn = ''
        for c in Dprev:            
            if c=='a':
                c = d['a']
            elif c=='b':                
                c = d['b']            
            Dn = Dn + c        
        Dprev = Dn
        print "Total Length of D%d : %d" %(i,len(Dn))
    return Dn

directionDict = {0:'N',1:'E',2:'S',3:'W'}

def getDirection(rank):
    """
        N
        |
    W---|---E
        |
        S
        N-0
        E-1
        S-2
        W-3
    """
    global directionDict
    rank = rank%4
    return directionDict[rank]
    
def main():
    x = 0
    y = 0
    n = int(raw_input("Enter Dn Value : "))
    MAX_STEP = int(raw_input("Enter Max Steps : "))
    verbose = int(raw_input("Verbose ? (1 or 0) : "))
    print "Obtaining D%d" % n
    dn = getDn(n)
    print "Total Characters in Dn : %s" % len(dn)
    print "Writing it to a file for future usage (d:\\temp\\heigidragon.txt)"
    file("d:\\temp\\heigidragon.txt","w").write(dn)
    curDir = 'N'
    step = 0
    rank = 0
    
    for c in dn:
        msg = ''
        msg = msg + "Current Char : " + c
        if c=='a' or c=='b':
            msg = msg + " :: Ignoring..."
            if verbose:
                print msg
            continue
        if c=='L':
            msg = msg + " :: Computing Rank..."
            rank = rank-1
        elif c=='R':
            msg = msg + " :: Computing Rank..."
            rank = rank+1
        elif c=='F':
            msg = msg + " :: Computing Direction "
            d = getDirection(rank)
            msg = msg + ":: " + d
            if d=='N':
                y = y+1
            elif d=='E':
                x = x+1
            elif d=='S':
                y = y-1
            elif d=='W':
                x = x-1
            step = step+1
            msg = msg + (":: Stepping Forward :: %d, %d" % (x,y))

        if verbose:
            print msg

        if step==MAX_STEP:
            print "Final Position : ",x,y
            break
    print "Final Position : ",x,y

if "__main__" == __name__:
    main()
            
        