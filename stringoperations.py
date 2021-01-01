#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'strng' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING fn
#  2. STRING ln
#  3. STRING para
#  4. INTEGER number
#

def stringoperation(fn, ln, para, number):
    # Write your code here
    print(fn+'\n'*number+ln)
    print(fn+'\t'+ln)
    print(fn*number)
    print("The sentence is "+para)

if __name__ == '__main__':

    fn = input()

    ln = input()

    para = input()

    no = int(input().strip())

    stringoperation(fn, ln, para, no)


