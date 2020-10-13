#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    largest_val = 0
    position = 0
    map={}
    
    for i in arr:
        if (i in map.keys()):
            map[i]+=1
        else:
            map[i]=1
       
    for i in map.keys():
        if(map[i]>largest_val):
            largest_val=map[i]
            position = i
        elif(map[i] == largest_val):
            if i < position:
                position = i
    
    return(position)
            
         
   

 


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
