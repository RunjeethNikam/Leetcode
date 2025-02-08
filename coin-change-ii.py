from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        coins.sort()
        for coin in coins:
            # if coin < (amount + 1):
            #     dp[coin] += 1
            for a in range(coin, amount + 1):
                dp[a] += dp[a - coin]
        return dp[-1]


print(Solution().change(amount=0, coins=[7]))
