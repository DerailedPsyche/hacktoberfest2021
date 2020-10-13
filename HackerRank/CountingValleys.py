import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    valley = 0
    level = 0
    flag = 0
    for i in s:
        if (i =="U" and flag == 0):
            level+=1
        elif(i=="D"):
            level-=1
            if(level<0):
                flag=1
        elif(i=="U" and flag == 1):
            level+=1
            if(level==0):
                valley+=1       
    return valley
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
