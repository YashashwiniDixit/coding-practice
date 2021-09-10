#https://www.hackerrank.com/contests/hackerrank-internship-challenges/challenges/diagonal-difference
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr,n):
    s1=0
    t=n
    s2=0
    # Write your code here
    for i in range(0,n):
        t-=1
        s1+=arr[i][i]
        s2+=arr[i][t]
    s1=abs(s1-s2)
    return s1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr,n)

    fptr.write(str(result) + '\n')

    fptr.close()
