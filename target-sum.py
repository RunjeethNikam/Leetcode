from typing import List
from functools import cache
from collections import defaultdict


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = defaultdict(int)
        dp[nums[0]] += 1
        dp[-nums[0]] += 1
        for num in nums[1:]:
            temp = dp.copy()
            dp.clear()
            for key, value in temp.items():
                dp[key + num] += value
                dp[key - num] += value
        return dp[target]

    
print(Solution().findTargetSumWays([0,0,1], 1))