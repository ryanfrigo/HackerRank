#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    jumps = 0
    i = 0
    while i < len(c):
        if len(c) > (i + 2) and c[i + 2] == 0:
            jumps += 1
            i += 2
        elif len(c) > (i + 1) and c[i + 1] == 0:
            jumps +=1
            i += 1
        else:
            return jumps

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
