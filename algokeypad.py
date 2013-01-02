import signal, os, string, math, time
import repeattimer
from matrix import *
from generalutils import *

KEY_MATRIX  = []
SEEDSTRING  = "abcd1234"
KEY_LEN     = 5
MAX_KEYS    = 1024 #Make this a perfect square
USER_KEY    = 0
KEY_SWITCH_DELAY = 10
STARTOFF = False    #Variable to make the program start at % 10 timestamp

DEBUG = False
FILE_LOG = False
f = None
if FILE_LOG:
    f = open("log.txt","w")

def handler():
    msg = "Current Key : %s" % str(calculateKeyCode())
    print msg
    if FILE_LOG:
        f.write(msg + "\n")



def calculateKeyCode():
    global KEY_MATRIX
    global SEEDSTRING
    global KEY_LEN
    global MAX_KEYS
    global DEBUG

    #Get the current time stamp
    #ts = int(time.time())
    ts = int(time.time())
    if FILE_LOG:
        f.write("Current Timestamp   : " + hex(ts) + "\n")
    ts = ts ^ USER_KEY
    if FILE_LOG:
        f.write("Converted Timestamp : " + hex(ts) + "\n")
    ts = hex(ts).replace('0x','')
    print "Operating TS : " + ts

    
    #time stamp is normally representable as a 4 byte hex value
    #ex : '0x4cada5e2'

    #Play with a copy    
    WORK_MATRIX = []
    for i in KEY_MATRIX:
        WORK_MATRIX.append(i)

    #Get all the bytes from ts
    byte0 = int(ts[-2:],16) & 0xF0      ####IGNORE THE LAST NIBBLE
    if(byte0 == 0x00):
        byte0 = 0xAD
    byte1 = int(ts[-4:-2],16)
    byte2 = int(ts[-6:-4],16)
    byte3 = int(ts[0:2],16)

    #Operations based on byte0 - SwapRows
    #If even, swap from top. If odd, swap from bottom
    WORK_MATRIX = swapRows(WORK_MATRIX,byte0,((byte0 + byte1) % 2 == 0))
    if FILE_LOG:
        f.write("Swapping Rows : " + str(byte0) + str(((byte0 + byte1) % 2 == 0)) + "\n")
        f.write(strMatrix(WORK_MATRIX))
    
    if DEBUG:
        print "Swap Rows : " + str(byte0)
        printMatrix(WORK_MATRIX)
    
    
    #Operations based on byte1 - SwapColumns
    #If even, swap from left. If odd, swap from right
    WORK_MATRIX = swapColumns(WORK_MATRIX,byte1,((byte0 + byte1) % 2 == 0))
    if FILE_LOG:
        f.write("Swapping Columns : " + str(byte1) + str(((byte0 + byte1) % 2 == 0)) + "\n")
        f.write(strMatrix(WORK_MATRIX))

    if DEBUG:
        print "Swap Columns : " + str(byte1)
        printMatrix(WORK_MATRIX)

    #Operations based on byte2 - Transpose
    #If abs(byte2 - byte 1) even, transpose. Else no action
    if(abs(byte2 - byte1) %2 == 0):
        WORK_MATRIX = transpose(WORK_MATRIX)

        if(FILE_LOG):        
            f.write("Transposing Matrix : ")
            f.write(strMatrix(WORK_MATRIX))
        
        if DEBUG:
            print "Transposed : " + str(byte2)
            printMatrix(WORK_MATRIX)
        

    #Operations based on byte3 - Get triangular elements
    #If abs(b3-b0)even : Get upper triangular elements
    #If odd : Get lower triangular elements
    li = []
    if(abs(byte3-byte0) % 2 == 0):
        li = getUpperTriangleElements(WORK_MATRIX)
        if(FILE_LOG):
            f.write("Upper Triangle Elements : ")
    else:
        li = getLowerTriangleElements(WORK_MATRIX)
        if (FILE_LOG):
            f.write("Upper Triangle Elements : ")

    #Now get the unique key code from the list
    #HOW?
    #. sum = (b3 + b2 + b1 + b0)
    # index = sum / b3 + sum / b2 + sum / b1 + sum / b0
    if(FILE_LOG):
        f.write(str(li) + '\n')
    sum = (byte3 + byte2 + byte1 + byte0)
    try:
        i = ((sum/byte3) + (sum / byte2) + (sum / byte1) + (sum / byte0))
    except:
        i = 0
    try:
        rval = li[i]
    except:
        rval = li[i % (len(li) - 1)]
    return rval

def prepare():
    """Prepares the KEY_MATRIX"""
    
    global KEY_MATRIX
    global SEEDSTRING
    global KEY_LEN
    global MAX_KEYS
    
    keys = nprString(SEEDSTRING, KEY_LEN)[0:MAX_KEYS]
    joinedkeys = [string.join(k,'') for k in keys]
    #Sort the string
    joinedkeys.sort()
    row = int(math.sqrt(MAX_KEYS))

    assert(row*row == MAX_KEYS)
    
    #Put the keys in the KEY_MATRIX
    cntr = 0
    for i in range(0,row):
        temp = []
        for j in range(0,row):
            temp.append(joinedkeys[cntr])
            cntr = cntr + 1
        KEY_MATRIX.append(temp)    


def starter():
    global STARTOFF
    ts = int(time.time())
    if (ts % 10 == 0):
        print ts
        if(FILE_LOG):
            f.write("Start Time Stamp : " + hex(ts))
        STARTOFF = True
    

def main():
    global KEY_MATRIX, KEY_SWITCH_DELAY, USER_KEY, STARTOFF
    USER_KEY = int(raw_input("Enter Key of your choice : "))
    prepare()
    print "Operating on the following Matrix : "
    printMatrix(KEY_MATRIX)
    if (FILE_LOG):
        f.write(strMatrix(KEY_MATRIX))
    print "Preparing to Start... "
    
    syncTimer = repeattimer.RepeatTimer(1.0,starter,100)
    syncTimer.start()
    
    while (STARTOFF == False):
        continue

    syncTimer.cancel()
    
    print "Started..."

    r = repeattimer.RepeatTimer(16.0,handler,100)
    r.start()

if __name__ == "__main__":
    main()