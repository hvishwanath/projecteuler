from utils import *

""" Sqrt(2) can be expressed as below :

1 + 1/2 + 2/5 + 4/11+ 8/23 + 16/47 .....

"""

#Start from 1/2
pn,pdn = 1,1
gn = 1

for i in range(1,10): #For 1000 expansions.
    if i == 1:
        gn = 1
        gdn = 2
    elif i == 2:
        gn = 2
        gdn = 5
        cx = 3
    else:
        cx = cx*2
        gn = gn*2
        gdn = gdn + cx
        
    expr = str(pn)+"/"+str(pdn)+"+"+str(gn)+"/"+str(gdn)
    nm,dn = fractionAdd(expr)
    pn = nm
    pdn = dn
    print i, expr, nm, dn
    