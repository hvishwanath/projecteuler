
def main():
    d = {
        1:'One',
        2:'Two',
        3:'Three',
        4:'Four',
        5:'Five',
        6:'Six',
        7:'Seven',
        8:'Eight',
        9:'Nine',
        10:'Ten',
        11:'Eleven',
        12:'Twelve',
        13:'Thirteen',
        14:'Fourteen',
        15:'Fifteen',
        16:'Sixteen',
        17:'Seventeen',
        18:'Eighteen',
        19:'Nineteen',
        20:'Twenty',
        30:'Thirty',
        40:'Forty',
        50:'Fifty',
        60:'Sixty',
        70:'Seventy',
        80:'Eighty',
        90:'Ninety',
        100:'One Hundred',
        200:'Two Hundred',
        300:'Three Hundred',
        400:'Four Hundred',
        500:'Five Hundred',
        600:'Six Hundred',
        700:'Seven Hundred',
        800:'Eight Hundred',
        900:'Nine Hundred',
        1000:'One Thousand' }

    for i in range(1,1001):
        if d.has_key(i):
            continue
        else:
            d = updateDict(i,d)
    l = 0
    print "Total Length of Dict : %d" % len(d)
    for v in d.values():
        v = v.replace(' ','')
        l = l + len(v)
    print "Total Characters used : %d" % l

def updateDict(i,d):
    x = str(i)
    if len(x) == 2:
        #2 Digit Numbers, 10 place
        remainder = i%10
        f = i-remainder
        fw = d[f]
        sw = d[remainder]
        fullword = fw + " " + sw
        d[i] = fullword
    elif len(x) == 3:
        #3 Digit Numbers, 100 place
        #Since we proceed in order, all 2 digit numbers
        #should already be in the dict.
        remainder = i%100
        f = i-remainder
        fw = d[f]
        sw = "and"
        tw = d[remainder]
        fullword = fw+" "+sw+" "+tw
        d[i] = fullword
    return d

if "__main__" == __name__:
    main()