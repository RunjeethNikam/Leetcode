from typing import List
from collections import defaultdict


class Solution:
    def maximumTotalCost(self, nums: List[int]) -> int:
        dp = defaultdict(int)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i - 1] + nums[i], dp[i - 2] + (nums[i - 1] + -nums[i]))
        return dp[len(nums) - 1]


print(Solution().maximumTotalCost(nums = [1,-1]))
