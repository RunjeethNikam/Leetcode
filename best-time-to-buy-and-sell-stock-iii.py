from typing import List
from collections import defaultdict


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def solve(index, holding, c):
            if index < len(prices) and c > 0:
                skip = solve(index + 1, holding, c)
                if holding:
                    ans = max(skip, prices[index] + solve(index + 1, False, c - 1))
                else:
                    ans = max(skip, -prices[index] + solve(index + 1, True, c))
                return ans

            return 0

        return solve(0, False, 2)


print(Solution().maxProfit(prices=[7, 6, 4, 3, 1]))
