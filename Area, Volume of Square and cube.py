#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'Integer_Math' function below.
#
# The function accepts following parameters:
#  1. INTEGER Side
#  2. INTEGER Radius
#

def Integer_Math(Side, Radius):
    # Write your code here
    pi = 3.14
    a = Side**2
    v = Side**3
    ac = pi * Radius * Radius
    vs = pi * Radius * Radius * Radius * 4/3
    
    print("Area of Square is", round(a,2))
    print("Volume of Cube is", round(v,2))
    print("Area of Circle is", round(ac,2))
    print("Volume of Sphere is", round(vs,2))

if __name__ == '__main__':
    Side = int(input().strip())

    Radius = int(input().strip())

    Integer_Math(Side, Radius)