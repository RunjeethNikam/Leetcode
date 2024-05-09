import math


class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0] * (n+1)
        dp[1] = 1
        largest_square = [1]
        for i in range(2,  n+1):
            sq = math.floor(math.sqrt(i)) 
            if (sq * sq) == i:
                largest_square.append(i)
                dp[i] = 1
            else:
                dp[i] = float('inf')
                for sq in largest_square:
                    dp[i] = min(dp[i], 1 + dp[i-sq])

        return dp[-1]

print(Solution().numSquares(15)) 
        