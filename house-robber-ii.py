from collections import defaultdict

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return max(nums)
        else:
            def solve(i,j):
                dp = defaultdict(int)
                for index in range(i,j+1):
                    dp[index] = max(dp[index-1], dp[index-2] + nums[index])
                return dp[j]

        return max(solve(1, len(nums)-1), nums[0] + solve(2, len(nums)-2))
    

print(Solution().rob([1,2,3,4]))