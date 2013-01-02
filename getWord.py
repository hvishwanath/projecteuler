import os
import string
from generalutils import *

DICT_FILE = "D:\\Harish Vishwanath\\Py\\ProjectEuler\\NewPythonProject\\src\\2of12.txt"


def getWord(s):
    """Pass a jumbled string. Prints a meaningful combination"""
    global DICT_FILE
    possibleList = permute(s)
    dictList = file(DICT_FILE).read().split('\n')
    cnt = 0
    for i in possibleList:
        if i in dictList:
            print i
            cnt = cnt + 1

    if (cnt == 0):
        print "No word found!"


def main():
    w = raw_input("Enter Jumbled Word : ")
    w = string.lower(w)
    getWord(w)

if __name__ == "__main__":
    main()
        