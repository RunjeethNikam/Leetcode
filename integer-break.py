class Solution:
    def integerBreak(self, n: int) -> int:
        dp = {1:1, 2:2}
        def solve(n):
            if n not in dp:
                max_product = 0
                for left in range(1, n):
                    max_product = max(max_product, solve(left) * solve(n - left))
                dp[n] = max(max_product, n)
            return dp[n]
        if n == 2:
            return 1
        if n == 3:
            return 2
        return solve(n)
    
print(Solution().integerBreak(5))