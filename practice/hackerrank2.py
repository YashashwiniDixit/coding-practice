#https://www.hackerrank.com/contests/hackerrank-internship-challenges/challenges/staircase/problem
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'staircase' function below.
#
# The function accepts INTEGER n as parameter.
#

def staircase(n):
    # Write your code here
    i=n-1
    x=' '
    while(i!=-1):
        for j in range(0,i):
            print(x,end="")
        for j in range(i,n):
            print("#",end="")
        i-=1
        print("")

if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
