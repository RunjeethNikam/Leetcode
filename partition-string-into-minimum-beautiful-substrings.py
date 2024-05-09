import math
class Solution:
    def minimumBeautifulSubstrings(self, s: str) -> int:
        def check_5(given):
            if given == 0:
                return False
            x = round(math.log(given) / math.log(5), 9) 
            return int(x) == x

        dp = [float('inf')] * len(s)
        for i in range(len(s)-1, -1, -1):
            if s[i] == '1':
                sm = 0
                for j in range(i, len(s)):
                    sm = (sm << 1) + int(s[j])
                    if check_5(sm):
                        dp[i] = min(dp[i], 1 + (dp[j+1] if (j+1) < len(dp) else 0))
            else:
                dp[i] = float('inf')

        return dp[0] if dp[0] != float('inf') else -1


print(Solution().minimumBeautifulSubstrings("10110111111011"))
# 1, 101, 11001, 1111101, 1001110001

