#!/bin/python3

import math
import os
import random
import re
import sys

class parent:
  def __init__(self,total_asset):
    self.total_asset = total_asset

  def display(self):
    print("Total Asset Worth is "+str(self.total_asset)+" Million.")
    print("Share of Parents is "+str(round(self.total_asset/2,2))+" Million.")


class son(parent):

    def __init__(self, total, val):

        parent.__init__(self, total)

        self.Percentage_for_son = val

    def son_display(self):

        x = self.Percentage_for_son * t/100

        x = round(x,2)

        print("Share of Son is {} Million.".format(x))

class daughter(parent):

    def __init__(self, total, val):

        parent.__init__(self, total)

        self.Percentage_for_daughter = val

    def daughter_display(self):

        x = self.Percentage_for_daughter * t/100

        x = round(x,2)

        print("Share of Daughter is {} Million.".format(x))

        

if __name__ == '__main__':
    
    t = int(input())
    sp = int(input())
    dp = int(input())


    obj1 = parent(t)
    

    obj2 = son(t,sp)
    obj2.son_display()
    obj2.display()


    obj3 = daughter(t,dp)
    obj3.daughter_display()
    obj3.display()
    
    print(isinstance(obj2,parent))
    print(isinstance(obj3,parent))

    print(isinstance(obj3,son))
    print(isinstance(obj2,daughter))