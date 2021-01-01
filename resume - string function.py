#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'resume' function below.
#
# The function is expected to print a STRING.
# The function accepts following parameters:
#  1. STRING first
#  2. STRING second
#  3. STRING parent
#  4. STRING city
#  5. STRING phone
#  6. STRING start
#  7. STRING strfind
#  8. STRING string1
#

def resume(first, second, parent, city, phone, start, strfind, string1):
    # Write your code here
    z=(first.strip().capitalize() +' '+ second.strip().capitalize() +' '+ parent.strip().capitalize() +' '+ city.strip())
    print(z)
    print(phone.isdecimal())
    print(phone.startswith(start))
    print(z.count(strfind))
    print(string1.split())
    print(city.find(strfind))

if __name__ == '__main__':

    a = input()

    b = input()

    c = input()

    d = input()

    ph = input()

    no = input()

    ch = input()

    str = input()

    resume(a, b, c, d, ph, no, ch, str)

