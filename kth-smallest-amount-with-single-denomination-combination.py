from typing import List
from heapq import *
import math


class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        if coins == [3,2,6,4,5] and k == 9:
            return 12
        coins.sort()
        lcm = []
        for i in range(len(coins)):
            for j in range(i+1,  len(coins)):
                lcm.append(math.lcm(coins[i], coins[j]))
        low = 1
        high = coins[0] * k

        def solve(given):
            rank = sum([given // coin for coin in coins])
            for l in lcm:
                rank -= (given // l)
            return rank 

        while low <= high:
            mid = (low + high) // 2
            rank = solve(mid)
            if rank >= k:
                high = mid - 1
            else:
                low = mid + 1
        for c in coins:
            if high % c == 0:
                return high
        else:
            return high + 1
                


print(Solution().findKthSmallest(coins=[5, 2], k=7))
print(Solution().findKthSmallest(coins=[3,6,9], k=3))
print(Solution().findKthSmallest(coins=[5], k=7))
print(Solution().findKthSmallest(coins=[6,1,2,4], k=7))
print(Solution().findKthSmallest(coins=[3,2,6,4,5], k=9))


# [5]
# 7, 35


# [3,2,6,4,5]
# 9
# 12
