from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        dp = [float('inf')] * (amount+1)
        dp[0] = 0
        for _ in coins:
            if _ < len(dp):
                dp[_] = 1

        for a in range(len(dp)):
            for coin in coins:
                if coin < a:
                    dp[a] = min(dp[a], dp[a-coin]+1)
        
        return dp[-1] if dp[-1] != float('inf') else -1
    
print(Solution().coinChange([1], 0))