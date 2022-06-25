#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):

    result = 0
    nivel = 0

    for i in s:
        if i=="D":
            nivel = nivel - 1
        elif i=="U":
            nivel = nivel + 1
        if i=="U" and nivel == 0:
            result = result + 1

    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()