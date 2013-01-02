#Given 1 Jan 1900 - Monday

MonthLegend = {
    'JAN':1,
    'FEB':2,
    'MAR':3,
    'APR':4,
    'MAY':5,
    'JUN':6,
    'JUL':7,
    'AUG':8,
    'SEP':9,
    'OCT':10,
    'NOV':11,
    'DEC':12
    }
DaysOf1900 = {
    1:'MON',
    2:'TUE',
    3:'WED',
    4:'THU',
    5:'FRI',
    6:'SAT',
    7:'SUN'
    }

DaysLegend = {
    1:31,
    2:59,
    3:90,
    4:120,
    5:151,
    6:181,
    7:212,
    8:243,
    9:273,
    10:304,
    11:334,
    12:365
    }
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

def calculateDays(dd,mm,yy):
    #Returns total number of elapsed days from 1 Jan 1900
    #dd,yy are integers. mm is String.
    #Accepts input of the form 1 Feb 2000
    days = 0
    ydiff = yy - 1900
    totalLeapYears = getNumberOfLeapYears(1900,yy)
    totalNonLeapYears = ydiff - totalLeapYears
    #print "Total Years Difference : %d " %ydiff
    #print "Total Leap Years : %d" % totalLeapYears
    #print "Total NonLeap Years : %d" % totalNonLeapYears
    days = (totalLeapYears * 366) + (totalNonLeapYears * 365)
    #print "Total Days sofar : %d" % days

    #Tackle the month
    mcode = MonthLegend[mm]-1
    #print "Total Months Difference : %d" % mcode
    if mcode != 0:
        days = days + DaysLegend[mcode]
        #print "After Adjusting Months, Total Days : %d" % days
        if mcode >= 2 and isLeapYear(yy):
            days = days + 1
            #print "This is a Leap Year., Adjusting : %d " % days

    #Tackle the Days            
    days = days + dd
    #print "After Adjusting Days, Total Days : %d" % days
    return days
        

def tellDay(dd,mm,yy):
    days = calculateDays(dd,mm,yy)
    index = days
    if days > 7:
        index = days % 7
        if index == 0:
            index= 7
    DAY = DaysOf1900[index]
    #print "%d %s %d was a %s" % (dd,mm,yy,DAY)
    return DAY
    
def main():
    mlist = ["JAN","FEB","MAR","APR","MAY","JUN","JUL","AUG","SEP","OCT","NOV","DEC"]
    cntr = 0
    for year in range(1901,2001):
        for m in mlist:
            if tellDay(1,m,year) == "SUN":
                cntr = cntr + 1
    print "Total Sundays falling on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000) : %d" % cntr

if "__main__" == __name__:
    main()