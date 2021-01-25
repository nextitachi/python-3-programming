#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'Magic_const' function below.
#
# 
#
# The function accepts INTEGER n1 as parameter.
#

def generator_Magic(n1):
    # Write your code here
   for i in range(3,n1+1):
        yield(int(i**3 + i)/2)
        


if __name__ == '__main__':

    n = int(input().strip())
    
    for i in generator_Magic(n):
        print(int(i))

    gen1 = generator_Magic(n)
    print(type(gen1))
