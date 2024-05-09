import math

class Solution:
    def minOperations(self, n: int) -> int:
        pows = [ 1<<i for i in range(math.ceil(math.log2(n))) ]
        result = 0
        while n:
            closes = min(pows, key=lambda p : abs(n-p))
            n = abs(n-closes)
            result += 1
        return result
        # dp = {1: 1}

        # def solve(given):
        #     i = 0
        #     if given in dp:
        #         return dp[given]
        #     while 2 ** (i+1) < given:
        #         i += 1
        #     if 2 ** (i + 1) == given:
        #         dp[given] = 1
        #         return 1
        #     else:
        #         dp[given] =  1 + min(solve(given - (2 ** i)), solve((2**(i + 1) - given)))
        #         return dp[given]

        # return solve(n)
    

print(Solution().minOperations(54))