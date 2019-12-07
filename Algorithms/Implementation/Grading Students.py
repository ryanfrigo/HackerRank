#!/bin/python3

import os
import sys

#
# Complete the gradingStudents function below.
#
def gradingStudents(grades):
    arr = []
    for g in grades:
        d = str(g)[-1:]
        if g < 38:
            arr.append(g)
        elif d == '3' or d == '4' or d == '8' or d == '9':
            while g % 5 != 0:
                g += 1
            arr.append(g)
        else:
            arr.append(g)
    return arr
        


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grades = []

    for _ in range(n):
        grades_item = int(input())
        grades.append(grades_item)

    result = gradingStudents(grades)

    f.write('\n'.join(map(str, result)))
    f.write('\n')

    f.close()
