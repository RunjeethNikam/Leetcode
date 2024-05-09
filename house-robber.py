from typing import List

class Solution:
    def get_index(self, nums, i):
        if i < 0:
            return 0
        else:
            return nums[i]

    def rob(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        for index, value in enumerate(nums):
            dp[index] = max(self.get_index(dp, index-1), self.get_index(dp, index-2) + value)
        return dp[-1]
    

print(Solution().rob([2,7,9,3,1]))