#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'generateList' function below.
#
# The function accepts following parameters:
#  1. INTEGER startvalue
#  2. INTEGER endvalue
#

def generateList(startvalue, endvalue):
    # Write your code here
    a = list(range(startvalue,endvalue+1))
    print (a[0:3])
    print (a[-1:-6:-1])
    print (a[::4])
    print (list(range(endvalue,startvalue-1,-2)))
    

if __name__ == '__main__':
    startvalue = int(input().strip())

    endvalue = int(input().strip())

    generateList(startvalue, endvalue)
