from collections import defaultdict


class Solution:
    def countOrders(self, n: int) -> int:
        MOD = 10**9 + 7
        dp = defaultdict(int)
        dp[1] = 1
        for i in range(2, n+1):
            spaces = i * 2
            dp[i] = ((dp[i-1] % MOD) * ((spaces-1) % MOD) * (i % MOD)) % MOD
        return dp[n] % MOD

print(Solution().countOrders(3))
