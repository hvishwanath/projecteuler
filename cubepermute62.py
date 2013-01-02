# To change this template, choose Tools | Templates
# and open the template in the editor.

"""
The cube, 41063625 (345^(3)), can be permuted to produce two other cubes:
56623104 (384^(3)) and 66430125 (405^(3)). In fact, 41063625 is the smallest cube
which has exactly three permutations of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits are cube.
"""

#Given 345 cube is smallest such cube. Start from 346.
from generalutils import nprString
from generalutils import *

cuberoot = 345
found = False
count = 0

while (1):
    count = 0
    start = cuberoot ** 3    
    #pList = permute(start)
    pList = nprString(str(start), len(str(start)))
    for number in pList:
        number = int(number)
        try:
            cube_root(number)
            count = count + 1
        except ValueError:
            pass
    cuberoot = cuberoot + 1
    if (count > 0):
        print "Number : %d, Cubes in Permutations %d" %(start, count)
    if (count == 5):
        break

__author__="HVISHWANATH"
__date__ ="$Aug 17, 2010 8:37:33 PM$"


if __name__ == "__main__":
    print "Hello World"
