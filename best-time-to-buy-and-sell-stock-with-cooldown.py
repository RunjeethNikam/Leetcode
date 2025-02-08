from typing import List


class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        # True = buy state, False = sell state
        def solve(index, status):
            if index >= len(prices):
                return 0

            if status:
                # We have buy in the past
                return max(
                    solve(index + 2, False) + prices[index],
                    solve(index + 1, status)
                )
            else:
                # We have selled in the past
                return max(
                    solve(index + 1, True) + -prices[index],
                    solve(index + 1, status),
                )


        return solve(0, False)



print(Solution().maxProfit(prices = [1]))
