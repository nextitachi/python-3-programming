#!/bin/python3

import math
import os
import random
import re
import sys



class comp:

    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
    def add(self, other):
        print("Sum of the two Complex numbers :",self.real+other.real, "+", self.imag+other.imag, "i", sep="")
    def sub(self, other):
        if self.imag-other.imag >= 0:
            print("Subtraction of the two Complex numbers :",self.real-other.real, "+", self.imag-other.imag, "i", sep="")
        else:
            print("Subtraction of the two Complex numbers :",self.real-other.real, "", self.imag-other.imag, "i", sep="")
if __name__ == '__main__':
    
    real1 = int(input().strip())
    img1 = int(input().strip())
    
    real2 = int(input().strip())
    img2 = int(input().strip())
    
    p1 = comp(real1,img1)
    p2 = comp(real2,img2)

    p1.add(p2)
    p1.sub(p2)
