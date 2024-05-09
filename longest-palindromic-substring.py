class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[0] * len(s) for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = 1
        
        for i in range(len(dp)-1, -1, -1):
            for j in range(len(dp[0])-1, -1, -1):
                if i <= j:
                    if i == j:
                        dp[i][j] = 1
                    elif s[i] == s[j]:
                        if i + 1 == j:
                            dp[i][j] = 2
                        elif dp[i+1][j-1] != 0:
                            dp[i][j] = dp[i+1][j-1] + 2
                        else:
                            dp[i][j] = 0
                    else:
                        dp[i][j] = 0
        
        mx = float('-inf')
        result = ""
        for i in range(len(dp)):
            for j in range(len(dp[0])):
                if dp[i][j] > mx:
                    mx = dp[i][j]
                    result = s[i:j+1]
        return result


print(Solution().longestPalindrome("aaaa"))