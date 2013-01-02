# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="HVISHWANATH"
__date__ ="$Aug 16, 2010 4:18:56 PM$"
import os

cipherFile = "cipher1.txt"
wordListFile = "2of12.txt"
outfile = "outfile.txt"
finalMsg = ''

from generalutils import *

def main():
    global finalMsg
    f = open(outfile,"w")
    #Read the cipher1 file.
    tx = file(cipherFile,"r").read().split(',')
    cipherText = [int(i) for i in tx]

    print "Cipher Text : %s" % cipherText
    os.system("pause")
    #Build Word list
    wordList = file(wordListFile,"r").read().split('\n')

    #Get possible 3 letter Keys.
    keyList = nprString("abcdefghijklmnopqrstuvwxyz",3)

    #keyList = [['o', 'r', 'e']]


    for key in keyList :
        #print "Processing For Key : ", key
        clearText = ''
        cntr = 0
        tmp = ''
        oneWordFound = False
        goodFirstChar = True
        msg = ''

        for asciiCode in cipherText:
            try:
                clearText = clearText + chr(ord(key[cntr]) ^ int(asciiCode))
            except Exception, ex:
                print str(ex)
                print key
                print cntr
                print ord(key[cntr])
                print int(asciiCode)
                
            cntr = cntr + 1
            if cntr == 3:
                cntr = 0
            if not str(clearText[0]).isalpha():
                if str(clearText[0]) not in ['"',' ','\'']:
                    print "First Char : %s" % str(clearText[0])
                    goodFirstChar = False
                    break
        #msg = "Current Key : %s\n Clear Text : \n%s\n\n" % (key,clearText)
        if goodFirstChar:
            msg = "%s\n" % (clearText)
            f.write(msg)
            #if (clearText != ' ' and ' ' in clearText):
            #    word = clearText.split()[0]
            #    if word in wordList:
            #        oneWordFound = True
            #        print "Current Key : %s, First Word : %s, Clear Text : %s" % (key,word,clearText)
            #        #raw_input("Hit a Key!")
            #    #else:
            #        #break
        #if oneWordFound:
            #print clearText
        
    f.close()

    

#if __name__ == "__main__":
#    main()
