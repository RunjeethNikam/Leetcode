from typing import List
from collections import Counter, deque
from heapq import *


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        dp = [0] * (max(nums)+1)
        for num in nums:
            dp[num] += num
        for i in range(1, len(dp)):
            if i == 1:
                dp[i] = max(dp[i-1], dp[i])
            elif i > 1:
                dp[i] = max(dp[i-1], dp[i-2]+dp[i])
        return dp[-1]

        
        


print(Solution().deleteAndEarn(nums=[2,3,4]))
