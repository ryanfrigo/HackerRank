#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    arr = sorted(arr)
    min = arr[0] + arr[1] + arr[2] + arr[3]
    max = arr[1] + arr[2] + arr[3] + arr[4]
    print(str(min) + " " + str(max))

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
