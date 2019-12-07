#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the viralAdvertising function below.

def viralAdvertising(n):
    liked = 0
    start = 5
    while (n > 0):
        liked += int(start/2)
        start = int(start/2)*3
        n -= 1
    return liked

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()
