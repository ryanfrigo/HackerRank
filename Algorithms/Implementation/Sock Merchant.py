#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    sox = {}
    pairs = 0
    for s in ar:
        if str(s) in sox:
            sox[str(s)] += 1
        else:
            sox[str(s)] = 1
    for key, value in sox.items():
        pairs += int(value/2)
    return pairs

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
