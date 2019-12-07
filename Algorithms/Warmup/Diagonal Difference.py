#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the diagonalDifference function below.
def diagonalDifference(arr):
    # row_len = 0
    # d1 = 0
    # d2 = 0
    # j = 2
    # for i in arr[0]:
    #     row_len += 1
    # for i in range(0, row_len):
    #     d1 += arr[i][i]
    #     d2 += arr[i][j]
    #     j -= 1
    # return abs(d1 - d2)
     return abs(sum(row[i] - row[-i-1] for i, row in enumerate(arr)))



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
