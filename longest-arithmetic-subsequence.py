from collections import defaultdict
from typing import List


class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)
        
        direction = None
        for index in range(1, len(nums)):
            difference = 
    # def longestArithSeqLength(self, nums: List[int]) -> int:
    #     dp = [defaultdict(int) for _ in range(len(nums))]
    #     for index, value in enumerate(nums):
    #         for j in range(index):
    #             diff = nums[j] - value
    #             dp[index][diff] = max(dp[index][diff], dp[j][diff] + 1) 
    #     result = 0
    #     for dd in dp:
    #         result = max(result, max(dd.values()))
    #     return result + 1
    

print(Solution().longestArithSeqLength([20,1,15,3,10,5,8]))
