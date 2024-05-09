from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [0] * len(prices)
        for sell_index, sell in enumerate(prices):
            for buy_index, buy in enumerate(prices[:sell_index]):
                last = 0
                if buy_index - 2 >= 0:
                    last = dp[buy_index - 2]
                if ((sell - buy) + last) > dp[sell_index]:
                    dp[sell_index] = (sell - buy) + last
        return max(dp)


print(Solution().maxProfit(prices = [1, 4, 2]))
