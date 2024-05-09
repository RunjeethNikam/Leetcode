from typing import List
from collections import defaultdict


class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = defaultdict(int)
        for value in arr:
            dp[value] = dp[value-difference] + 1
        return max(dp.values())
    
print(Solution().longestSubsequence([1,5,7,8,5,3,4,2,1], -2))