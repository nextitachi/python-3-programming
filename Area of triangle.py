#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'tria' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. FLOAT n1
#  2. FLOAT n2
#  3. INTEGER n3
#
from math import pi
def triangle(n1, n2, n3):
    # Write your code here
    area = float(n1*n2/2)
    return (round(area,n3), round(pi,n3))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n1 = float(input().strip())

    n2 = float(input().strip())

    n3 = int(input().strip())

    result = triangle(n1, n2, n3)

    fptr.write(str(result) + '\n')

    fptr.close()
