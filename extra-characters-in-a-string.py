from typing import List
from collections import defaultdict


class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:

        t = {}
        for word in dictionary:
            temp = t
            for ch in word[::-1]:
                if ch not in temp:
                    temp[ch] = {}
                temp = temp[ch]
            temp['*'] = '-'
            

        dp = [float("inf")] * len(s)
        for i in range(len(s)):
            temp = t
            for j in range(i, -1, -1):
                if s[j] in temp:
                    temp = temp[s[j]]
                    if '*' in temp:
                        dp[i] = min(dp[i], dp[j - 1] if (j - 1) >= 0 else 0)
                    else:
                        dp[i] = min(dp[i], (dp[j - 1] if (j - 1) >= 0 else 0) + (i-j+1))    
                else:
                    dp[i] = min(dp[i], (dp[j - 1] if (j - 1) >= 0 else 0) + (i-j+1))
                    break
        return dp[-1]


print(
    Solution().minExtraChar(
        "sleet",
        ["leet"],
    )
)
