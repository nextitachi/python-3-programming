#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'sumOfNFibonacciNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def sumOfNFibonacciNumbers(n):
    # Write your code here
    if (n <= 1) : 
        return 0
   
    fibo =[0] * (n+1) 
    fibo[1] = 1
   
    # Initialize result 
    sm = fibo[0] + fibo[1] 
   
    # Add remaining terms 
    for i in range(2,n) : 
        fibo[i] = fibo[i-1] + fibo[i-2] 
        sm = sm + fibo[i] 
          
    return sm     

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = sumOfNFibonacciNumbers(n)

    fptr.write(str(result) + '\n')

    fptr.close()
