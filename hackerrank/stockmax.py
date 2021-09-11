#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'stockmax' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY prices as parameter.
#

def stockmax(p):
    ind_max = p.index(max(p))
    inv = sum(p[:ind_max])
    pf = len(p[:ind_max])*p[ind_max] - inv
    if len(p[ind_max+1:]) > 0:
        pf += stockmax(p[ind_max+1:])
    return pf

        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        prices = list(map(int, input().rstrip().split()))

        result = stockmax(prices)

        fptr.write(str(result) + '\n')

    fptr.close()
#https://www.hackerrank.com/challenges/stockmax/problem
