class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = 10**9 + 7
        dp = [[0] * (target + 1) for _ in range(n + 1)]
        for dice in range(1, n + 1):
            for face in range(1, min(k + 1, target + 1)):
                if dice != 1:
                    for t in range(face + 1, target + 1):
                        dp[dice][t] = (
                            dp[dice][t] % MOD + dp[dice - 1][t - face] % MOD
                        ) % MOD
                else:
                    dp[dice][face] = 1

        return dp[n][target] % MOD


print(Solution().numRollsToTarget(n=30, k=30, target=500))
