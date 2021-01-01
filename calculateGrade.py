#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'calculateGrade' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts 2D_INTEGER_ARRAY students_marks as parameter.
#

def calculateGrade(students_marks):
    # Write your code here
    Gra=[]
    for grade_list in students_marks:
        total=sum(grade_list)
        av=float(total/(len(grade_list)))
        if av >=90:
            Grades='A+'
        elif av >=80 and av <90:
            Grades='A'
        elif av >=70 and av <80:
            Grades='B'
        elif av >=60 and av <70:
            Grades='C'
        elif av >=50 and av <60:
            Grades='D'
        elif av <50:
            Grades='F'
        Gra.append(Grades)
    return(Gra)
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    students_marks_rows = int(input().strip())
    students_marks_columns = int(input().strip())

    students_marks = []

    for _ in range(students_marks_rows):
        students_marks.append(list(map(int, input().rstrip().split())))

    result = calculateGrade(students_marks)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
