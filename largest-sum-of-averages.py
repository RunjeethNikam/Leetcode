from typing import List
from functools import lru_cache


class Solution:

    # def largestSumOfAverages(self, nums: List[int], k: int) -> float:
    #     @lru_cache(None)
    #     def solve(i, k):
    #         if i < 0 or k > (i + 1):
    #             return None

    #         if k == 1:
    #             return sum(nums[: i + 1]) / (i + 1)

    #         if (i+1) == k:
    #             return sum(nums[: i + 1])

    #         mx = -1
    #         sm = 0
    #         count = 0

    #         for index in range(i, k - 2, -1):
    #             sm += nums[index]
    #             count += 1
    #             temp = solve(index-1, k-1)
    #             if temp:
    #                 mx = max(mx, temp + (sm/count))

    #         return mx

    #     return solve(len(nums) - 1, k)

    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        dp = [[0] * len(nums) for _ in range(2)]
        sm = 0
        for index in range(len(nums)):
            if (index+1) <= k:
                sm += nums[index]
                dp[index] = sm
            else:
                sm = 0
                count = 0
                for i2 in range(index, k-2, -1):
                    sm += 


# print(Solution().largestSumOfAverages([4, 1, 7, 5, 6, 2, 3], 4))
print(Solution().largestSumOfAverages([2927,2898,6670,1318,2273,8956,1410], 5))
