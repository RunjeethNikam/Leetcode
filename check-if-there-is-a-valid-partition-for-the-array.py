from typing import List


class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        dp = [False] * len(nums)

        for index, value in enumerate(nums):
            if index > 0:
                if value == nums[index-1]:
                    dp[index] = dp[index] or (dp[index-2] if (index-2) >= 0 else True)
                if index > 1 and value == nums[index-1] and value == nums[index-2]:
                    dp[index] = dp[index] or (dp[index-3] if (index-3) >= 0 else True)
                if index > 1 and (value-1) == nums[index-1] and (value-2) == nums[index-2]:
                    dp[index] = dp[index] or (dp[index-3] if (index-3) >= 0 else True)
        return dp[-1]

print(Solution().validPartition([1,1,1,2]))