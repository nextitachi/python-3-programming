#!/bin/python3

import math
import os
import random
import re
import sys

from pprint import pprint as print

#
# Complete the 'myDict' function below.
#
# The function accepts following parameters:
#  1. STRING key1
#  2. STRING value1
#  3. STRING key2
#  4. STRING value2
#  5. STRING value3
#  6. STRING key3
#

def myDict(key1, value1, key2, value2, value3, key3):
    # Write your code here
    a = {key1:value1}
    print (a)
    a[key2]=value2
    print (a)
    a[key1]=value3
    print(a)
    del a[key3]
    return a

if __name__ == '__main__':
    key1 = input()

    value1 = input()

    key2 = input()

    value2 = input()

    value3 = input()

    key3 = input()

    mydct = myDict(key1, value1, key2, value2, value3, key3)
    
    print(mydct if type(mydct) == dict else "Return a dictionary")
    
    
