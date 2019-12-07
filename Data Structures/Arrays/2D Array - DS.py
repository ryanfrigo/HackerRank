#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglass(arr, row, col):
    res = []
    res.append(arr[row][col])
    res.append(arr[row][col + 1])
    res.append(arr[row][col + 2])
    res.append(arr[row + 1][col + 1])
    res.append(arr[row + 2][col])
    res.append(arr[row + 2][col + 1])
    res.append(arr[row + 2][col + 2])
    return res

def hourglassSum(arr):
    sums = []
    for i in range(0, (len(arr)-2)):
        for j in range(0, (len(arr[0])-2)):
            sums.append(sum(hourglass(arr, i, j)))
    return max(sums)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
