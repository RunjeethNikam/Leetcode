from typing import List
from collections import defaultdict


class Solution:

    def maxSelectedElements(self, nums: List[int]) -> int:
        dp = [0] * (max(nums) + 2)

        for i in nums:
            dp[i] = 1

        for i in range(1, len(dp)):
            if (i + 1) < len(dp):
                dp[i + 1] = (dp[i]-1)  + 1
            dp[i] = dp[i-1] + 1
        
        return max(dp)
    

print(Solution().maxSelectedElements([2,1,5,1,1]))