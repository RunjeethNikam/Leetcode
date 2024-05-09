class Solution:
    def numTrees(self, n: int) -> int:
        dp = {}
        dp[0] = 1
        dp[1] = 1
        dp[2] = 2

        def f(n):
            if n not in dp:
                result = 0
                for left in range(n):
                    right = n - left - 1
                    result += f(left) * f(right)
                dp[n] = result
            return dp[n]
        
        return f(n)


print(Solution().numTrees(3))
