from os import *
from sys import *
from collections import *
from math import *

def tossStrangeCoins(prob, target):

    if target == 0:
        return prod(map(lambda _: 1-_, prob))
    if target == len(prob):
        return prod(prob)
    


    dp= [[0] * len(prob) for _ in range(2)]
    dp[0][0] = prob[0]
    dp[1][0] = 1-prob[0]

    for c in range(1, len(prob)):
        if c < target:
            dp[0][c] = dp[0][c-1] * prob[c]
            dp[1][c] = dp[0][c-1] * (1-prob[c])
        else:
            dp[0][c] = prob[c] * dp[1][c-1]
            dp[1][c] = (1-prob[c]) * dp[0][c-1]
    print(dp)

print(tossStrangeCoins([0.44, 0.51], 2))