from pprint import pprint

class Solution:
    def knightDialer(self, n: int) -> int:
        if n == 1:
            return 10
        MOD = 10**9 + 7
        mapping = {
            0: [4, 6],
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [3, 9, 0],
            5: [],
            6: [1, 7, 0],
            7: [6, 2],
            8: [1, 3],
            9: [4, 2],
        }
        dp = [[0 for __ in range(10)] for _ in range(n+1)]
        dp[1][0]=1
        dp[1][1]=1
        dp[1][2]=1
        dp[1][3]=1
        dp[1][4]=1
        dp[1][6]=1
        dp[1][7]=1
        dp[1][8]=1
        dp[1][9]=1
        for steps in range(1, n+1):
            for start in range(10):
                for next_step in mapping[start]:
                    dp[steps][start] = (dp[steps][start] % MOD + dp[steps-1][next_step] % MOD) % MOD
        return sum(dp[-1]) % MOD

print(Solution().knightDialer(3131))

