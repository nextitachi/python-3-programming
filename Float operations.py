#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'Float_fun' function below.
#
# The function accepts following parameters:
#  1. FLOAT f1
#  2. FLOAT f2
#  3. INTEGER Power
#

def Float_fun(f1, f2, Power):
    # Write your code here
    print("#Add")
    print(f1+f2)
    print("#Subtract")
    print(f1-f2)
    print("#Multiply")
    print(f2*f1)
    print("#Divide")
    print(f2/f1)
    print("#Remainder")
    print(f1 % f2)
    print("#To_The_Power_Of")
    print(f1 ** Power)
    print("#Round")
    print(round(f1 ** Power, 4))
    

if __name__ == '__main__':
    f1 = float(input().strip())

    f2 = float(input().strip())

    Power = int(input().strip())

    Float_fun(f1, f2, Power)