from typing import List
from collections import defaultdict


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        dp = defaultdict(lambda: defaultdict(int))
        count = 0
        for i, value in enumerate(nums):
            for j in range(i):
                diff = value - nums[j]
                count += dp[j][diff]
                dp[i][diff] += dp[j][diff] + 1
        return count


print(Solution().numberOfArithmeticSlices(nums=[2, 4, 6, 8, 10]))
