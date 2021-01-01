#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'tuplefun' function below.
#
# The function accepts following parameters:
#  1. LIST list1
#  2. LIST list2
#  3. STRING string1
#  4. INTEGER n
#

def tuplefunction(list1, list2, string1, n):
    # Write your code here
    tuple1=tuple(list1)
    tuple2=tuple(list2)
    t = tuple(tuple1 + tuple2)
    print (t)
    print (t[4])
    t2 = (tuple1, tuple2)
    print(t2)
    print(len(t2))
    print (tuple((string1,))*n)
    print(max(tuple1))
    
    
if __name__ == '__main__':
    
    qw1_count = int(input().strip())

    qw1 = []

    for _ in range(qw1_count):
        qw1_item = int(input().strip())
        qw1.append(qw1_item)

    qw2_count = int(input().strip())

    qw2 = []

    for _ in range(qw2_count):
        qw1_item = input()
        qw2.append(qw1_item)
        
    str1 = input()

    n = int(input().strip())

    tuplefunction(qw1,qw2,str1, n)
