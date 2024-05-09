from typing import List

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target+1)
        for num in nums:
            if num < len(dp):
                dp[num] += 1
        for i in range(target+1):
            for j in nums:
                if j < i:
                    dp[i] += dp[i-j]

        return dp[-1]

print(Solution().combinationSum4([9], 3))