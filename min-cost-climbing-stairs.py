from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp1 = 0
        dp2 = 0
        i = 2
        while i < len(cost)+1:
            temp = min(dp2 + cost[i-1], dp1 + cost[i-2])
            dp1 = dp2
            dp2 = temp
            i += 1
        return dp2
print(Solution().minCostClimbingStairs([10,15,20])) 