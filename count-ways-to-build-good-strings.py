class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        dp = [0] * (high + 1)
        dp[zero] = 1
        dp[one] += 1
        for i in range(len(dp)):
            if i >= zero:
                dp[i] += dp[i-zero]
            if i >= one:
                dp[i] += dp[i-one]
        return sum(dp[low:])
    

print((Solution().countGoodStrings(2,3,1,2)))