from functools import cache


class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 10**9 + 7
        dp = [[0, 0] for _ in range(n + 1)]
        dp[0] = [1, 0]
        dp[1] = [1, 0]
        for i in range(2, n + 1):
            result = 0
            result += dp[i - 1][1] % MOD
            result += dp[i - 1][0] % MOD
            result += dp[i - 2][0] % MOD
            dp[i][0] = result % MOD

            result = 0
            result += 2 * dp[i - 2][0] % MOD
            result += dp[i - 1][1] % MOD
            dp[i][1] = result % MOD

        return dp[-1][0] % MOD


print(Solution().numTilings(5))
