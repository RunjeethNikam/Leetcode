from typing import List
from collections import defaultdict
from math import sqrt


class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        dp = defaultdict(int)
        for num in nums:
            dp[num] = 1 + dp[num * num]
        result = max(dp.values())
        return result if result >= 2 else -1
    
print(Solution().longestSquareStreak([2,3,5,6,7]))

