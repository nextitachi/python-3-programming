#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'calc' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER c as parameter.
#
from math import pi

def calc(c):
    # Write your code here
    radius = float( c / (math.pi * 2) )

    area = float(math.pi * radius ** 2)
    
    return (round(radius,2), round(area,2))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    c = int(input().strip())

    result = calc(c)

    fptr.write(str(result) + '\n')

    fptr.close()
