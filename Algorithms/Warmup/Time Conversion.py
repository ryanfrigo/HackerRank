#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    pm = 0
    if s[0:2] == "12":
        if s[-2:] == "AM":
            return ("00" + s[2:8])
        else:
            return ("12" + s[2:8])
    if s[-2:] == "PM":
        pm = 1
    if pm == 0:
        return s[0:8]
    else:
        return str(int(s[0:2]) + 12) + s[2:8]

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
