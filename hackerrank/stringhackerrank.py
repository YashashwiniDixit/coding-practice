#!/bin/python

import math
import os
import random
import re
import sys

#
# Complete the 'stringConstruction' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def stringConstruction(s):
    # Write your code here
    l=[]
    for i in s:
        l.append(i)
    l=list(set(l))
    print(l)
    l1=len(l)
    return l1
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(raw_input().strip())

    for q_itr in xrange(q):
        s = raw_input()

        result = stringConstruction(s)

        fptr.write(str(result) + '\n')

    fptr.close()
#https://www.hackerrank.com/challenges/string-construction/problem
