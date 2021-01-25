#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'strmethod' function below.
#
# The function accepts following parameters:
#  1. STRING para
#  2. STRING spch1
#  3. STRING spch2
#  4. LIST li1
#  5. STRING strf
from collections import Counter
def stringmethod(para, special1, special2, list1, strfind):
    # Write your code here
    word1 = ''.join([i  for i in para if i not in special1] )
    # print( special1)
    rword2 = word1[:70]
    rword2 = rword2[::-1]
    print(rword2)
    
    rjoin = special2.join(rword2.replace(" ",""))
    print(rjoin)
    
    if all(  x in para for x in list1  ):
        print(f"Every string in  {list1} were present")
    else:
        print(f"Every string in  {list1} were not present")
    
    a = word1.split()
    print(a[:20])
    
    l = word1.split()
    f = Counter(l)
    temp =[]
    for k,v in f.items():
        if  v < 3:
            temp.append(k)
    print(temp[-20:])
    
    print(word1.rfind(strfind))

if __name__ == '__main__':
    para = input()

    spch1 = input()

    spch2 = input()
    
    qw1_count = int(input().strip())

    qw1 = []

    for _ in range(qw1_count):
        qw1_item = input()
        qw1.append(qw1_item)

    strf = input()

    stringmethod(para, spch1, spch2, qw1, strf)
