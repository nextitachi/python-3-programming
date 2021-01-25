#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'primegenerator' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER num
#  2. INTEGER val
#
import sympy
def primegenerator(num, val):
    pn = list(sympy.primerange(2,num+1))
    if val == 0:
        a=(pn[1::2])
    if val == 1:
        a=(pn[::2])
    
    for b in a:
        return (a)

if __name__ == '__main__':

    num = int(input().strip())

    val = int(input().strip())

    for i in primegenerator(num, val):
        print(i,end=" ")