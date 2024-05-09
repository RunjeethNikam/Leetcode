class Solution:
    def numDecodings(self, s: str) -> int:
        
        if s.startswith('0'):
            return 0
        
        allowed = set(map(lambda _: str(_), range(1, 27)))
        dp = [0] * len(s)
        for i in range(len(s)):
            if s[i] in allowed:
                dp[i] += (dp[i-1] if i > 0 else 1)
            if i > 0 and s[i-1: i+1] in allowed:
                dp[i] += (dp[i-2] if i > 1 else 1)
        return dp[-1]


print(Solution().numDecodings("1"))
