#!/bin/python3

# Score:18.42
# Status:Wrong Answer
# Fails the following test cases: 2 7 8 11 12

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    count = 0
    for word in magazine:
        if word in note:
            count += 1
    if count >= len(note):
        print("Yes")
        return "Yes"
    else:
        print("No")
        return "No"

if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
