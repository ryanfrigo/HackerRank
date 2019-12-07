#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    repeat = int(n / len(s))
    remainder = n % len(s)
    a_chars = s.count('a')
    a_remainder = s[0:remainder].count('a')
    result = a_chars * repeat + a_remainder
    return(result)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
