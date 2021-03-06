
import math
import os
import random
import re
import sys

#
# Complete the 'pairs' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def pairs(k, arr):
    n=len(arr)
    arr.sort()
    left=1
    right=0
    count=0
    while left<n:
        print(left,right)
        diff=arr[left]-arr[right]
        if diff<k:
            left+=1
        if diff>k:
            right+=1
        if diff==k:
            count+=1
            left+=1
        return count
    
   
#def pairs(k, arr):
#    set1 = set(arr)
#    set2 = [value + k for value in arr]
#    return len(set1.intersection(set2))

        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
