#!/bin/python3

import math
import os
import random
import re
import sys



# Write your code here
class Movie:

    def __init__(self, val1, val2, val3):

        self.movieName= val1

        self.numberTickets = val2

        self.totalCost = val3

    def __str__(self):

        #return self.movieName

        #return self.numberTickets

        #return self.totalCost

        return "Movie : {}\nNumber of Tickets : {}\nTotal Cost : {}".format(self.movieName,self.numberTickets,self.totalCost)

if __name__ == '__main__':
    name = input()
    n = int(input().strip())
    cost = int(input().strip())
    
    p1 = Movie(name,n,cost)
    print(p1)

