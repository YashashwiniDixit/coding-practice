#https://www.hackerrank.com/contests/hackerrank-internship-challenges/challenges/time-conversion/problem
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    l=len(s)
    s1=s[-2:l]
    s3=""
    if s1=='PM':
        if s[0:2]=='12':
            return s[0:8]
        h=12
        h2=int(s[0:2])
        h+=h2
        h=str(h)
        s3=h+":"+s[3:8]
        return s3
    if s1=='AM':
        if s[0:2]=='12':
            s3="00:"+s[3:8]
            return s3
        s3=s[0:8]
        return s3
    return s3

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
