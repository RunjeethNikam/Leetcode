from typing import List
from functools import cache
from collections import defaultdict


class Solution:
    # def splitArray(self, nums: List[int], k: int) -> int:
    #     @cache
    #     def solve(index, k):
    #         if k == 1:
    #             return sum(nums[: index + 1])
    #         sm = 0
    #         result = float("inf")
    #         for i in range(index, k-2, -1):
    #             sm += nums[i]
    #             result = min(result, max(solve(i - 1, k - 1), sm))
    #         return result

    #     return solve(len(nums) - 1, k)

    def splitArray(self, nums: List[int], k: int) -> int:
        dp = defaultdict(int)
        for j, value in enumerate(nums):
            dp[(j, k)] = max(dp[(j - 1, k - 1)], value)
            for i in range(j, -1, -1):
                value += nums[i]
                dp[(j, k)] = max(dp[(i - 1, k - 1)], value)
        return dp[(len(nums) - 1, k)]


print(Solution().splitArray([1, 4, 4], 3))
