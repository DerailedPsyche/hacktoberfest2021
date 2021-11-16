# Link to problem: https://www.hackerrank.com/challenges/marcs-cakewalk/

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the marcsCakewalk function below.
def marcsCakewalk(calorie):
    calorie.sort(reverse = True)
    sm = 0
    j = 0
    for i in calorie:
        sm += ((2 **j) * i)
        j += 1
    return sm

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    calorie = list(map(int, input().rstrip().split()))

    result = marcsCakewalk(calorie)

    fptr.write(str(result) + '\n')

    fptr.close()
