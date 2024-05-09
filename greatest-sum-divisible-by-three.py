from typing import List
from collections import defaultdict


class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        dp = [0]
        # dp = defaultdict(bool)
        for num in nums:
            if (dp[-1] + num) % 3 =
            # for k in list(dp.keys()):
            #     dp[k + num] = True
            # dp[num] = True
        return max([i for i in dp.keys() if i % 3 == 0] + [0])


print(Solution().maxSumDivThree([1,2,3,4,4]))
