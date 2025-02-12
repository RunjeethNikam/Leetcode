from typing import List
from functools import cache
from collections import defaultdict


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = defaultdict(int)
        for index in range(len(days) - 1, -1, -1):
            cost = float('inf')
            for d, c in zip([1, 7, 30], costs):
                t = index + 1
                while t < len(days) and (days[index] + d) > days[t]:
                    t += 1
                cost = min(dp[t] + c, cost)
            dp[index] = cost
        return dp[0]
        # @cache
        # def solve(index):
        #     if index == len(days):
        #         return 0
        #     cost = float('inf')
        #     for d, c in zip([1, 7, 30], costs):
        #         t = index + 1
        #         while t < len(days) and (days[index] + d) > days[t]:
        #             t += 1
        #         cost = min(solve(t) + c, cost)
        #     return cost
                
    

        # return solve(0)


print(Solution().mincostTickets(days = [1,4,6,7,8,20], costs = [2,7,15]))
