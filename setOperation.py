#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'setOperation' function below.
#
# The function is expected to return a union, intersection, difference(a,b), difference(b,a), symmetricdifference and frozen set.
# The function accepts following parameters:
#  1. List seta
#  2. List setb
#

def setOperation(seta, setb):
    # Write your code here
    sa = set(seta)
    sb = set(setb)
    s1 = list((sa.union(sb)))
    s2 = list((sa.intersection(sb)))
    s3 = list((sa.difference(sb)))
    s4 = list((sb.difference(sa)))
    s5 = list((sa.symmetric_difference(sb)))
    x = frozenset(seta)
    return (s1, s2, s3, s4, s5, x)


if __name__ == '__main__':
    seta_count = int(input().strip())

    seta = []

    for _ in range(seta_count):
        seta_item = input()
        seta.append(seta_item)

    setb_count = int(input().strip())

    setb = []

    for _ in range(setb_count):
        setb_item = input()
        setb.append(setb_item)

    un, intersec, diffa, diffb, sydiff, frset = setOperation(seta, setb)
    print(sorted(un))
    print(sorted(intersec))
    print(sorted(diffa))
    print(sorted(diffb))
    print(sorted(sydiff))
    print("Returned value is {1} frozenset".format(frset, "a" if type(frset) == frozenset else "not a"))