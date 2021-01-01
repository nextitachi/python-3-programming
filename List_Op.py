#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'List_Op' function below.
#
# The function accepts following parameters:
#  1. LIST Mylist
#  2. LIST Mylist2
#

def List_Op(Mylist, Mylist2):
    # Write your code here
    print(Mylist)
    print(Mylist[1])
    print(Mylist[-1])
    Mylist.append(3)
    Mylist[3]=60
    print(Mylist)
    print(Mylist[1:5])
    Mylist.append(Mylist2)
    print(Mylist)
    Mylist.extend(Mylist2)
    print(Mylist)
    Mylist.pop()
    print(Mylist)
    print(len(Mylist))
    

if __name__ == '__main__':
    qw1_count = int(input().strip())

    qw1 = []

    for _ in range(qw1_count):
        qw1_item = int(input().strip())
        qw1.append(qw1_item)

    qw2_count = int(input().strip())

    qw2 = []

    for _ in range(qw2_count):
        qw1_item = int(input().strip())
        qw2.append(qw1_item)

    List_Op(qw1,qw2)