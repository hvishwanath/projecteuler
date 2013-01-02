from utils import *


rep1 = []
rep2 = []
rep3 = []
rep4 = []
rep5 = []
rep6 = []
rep7 = []
rep8 = []
rep9 = []
rep0 = []

ldict = {
    0:rep0,
    1:rep1,
    2:rep2,
    3:rep3,
    4:rep4,
    5:rep5,
    6:rep6,
    7:rep7,
    8:rep8,
    9:rep9
}

def main():
    li = getPrimeList(1000,100000)

    #Categorize the prime list into repeat lists.
    for item in li:
        d = repeats(item)
        for key in d.keys():
            ldict[key].append(item)

    tlist = []
    for v in ldict.values():
        tlist.append(len(v))
    maxlen = max(tlist)
    s = "%7s\t\t%7s\t\t%7s\t\t%7s\t\t%7s\t\t%7s\t\t%7s\t\t%7s\t\t%7s\t\t%7s\n" % ("LIST0",
                                                                                  "LIST1",
                                                                                  "LIST2",
                                                                                  "LIST3",
                                                                                  "LIST4",
                                                                                  "LIST5",
                                                                                  "LIST6",
                                                                                  "LIST7",
                                                                                  "LIST8",
                                                                                  "LIST9")
    s = s+"----------------------------------------------------------------------------------------\n\n"

        
    for i in range(0,maxlen):
        for v in ldict.values():
            try:
                x = "%7d\t\t" % v[i]
            except:
                x = "%7s\t\t" % ' '
            s = s + x
        s = s + "\n"
    file("d:\\temp\\p51.txt","w").write(s)
            

if "__main__" == __name__:
    main()
                