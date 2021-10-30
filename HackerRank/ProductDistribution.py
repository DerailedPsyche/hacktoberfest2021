# Link to problem: https://www.hackerrank.com/contests/hacktheinterview3/challenges/distribution-in-m-bins


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maxScore' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER m
#

def maxScore(a, m):
    # Write your code here
    a.sort(reverse =True)
    temp = 0
    ans = 0
    i = 1
    t = m    
    while len(a) >= m:
        if t == 0:
            ans += (temp) * i
            i += 1
            t = m
            temp = 0
        temp += a.pop()
        t -= 1
    while a:
        temp += a.pop()
    
    ans += temp * (i)
    ans =ans % ((10**9) + 7) 
    return ans 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    a = list(map(int, input().rstrip().split()))

    ans = maxScore(a, m)

    fptr.write(str(ans) + '\n')

    fptr.close()
