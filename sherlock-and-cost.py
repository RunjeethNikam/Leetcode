#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cost' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY B as parameter.
#

def cost(B):
    dp = [[0,0] * len(B)]
    for index in range(1, len(B)):
        dp[index][0] = max(abs(B[index]-1)+dp[index-1][1], abs(B[index]-1) + dp[index-1][0])
        dp[index][1] = max(abs(B[index-1]-1)+dp[index-1][1], abs(B[index-1]-1) + dp[index-1][0])
    return max(dp[-1])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        B = list(map(int, input().rstrip().split()))

        result = cost(B)

        fptr.write(str(result) + '\n')

    fptr.close()
