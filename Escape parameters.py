#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'Escape' function below.
#
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#  3. STRING s3
#

def Escape(s1, s2, s3):
    # Write your code here
    s = "Python\tRaw\nString\tConcept"
    print(s1+'\n'+s2+'\n'+s3)
    print(s1+'\t'+s2+'\t'+s3)
    print(s)
    raw_s = r"Python\tRaw\nString\tConcept"
    print(raw_s)

if __name__ == '__main__':
    s1 = input()

    s2 = input()

    s3 = input()

    Escape(s1, s2, s3)