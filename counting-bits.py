from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0, 1]
        i = 2
        while i < (n+1):
            x = i >> 1
            dp.append(dp[x] + 1)
            i += 1
        return dp
    
print(Solution().countBits(5))