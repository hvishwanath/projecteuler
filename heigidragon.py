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

def getDn(n):
    D0 = "Fa"
    if n==0:
        return D0
    Dprev = D0
    for i in range(1,n+1):
        Dn = Dprev.replace('a',d[a])
        Dn = Dn.replace('b',d[b])
        Dprev = Dn
    return Dn