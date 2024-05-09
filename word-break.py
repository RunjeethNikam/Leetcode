from typing import List

class Solution:

    def check(self, s, i, word):
        j = 0
        while i < len(s) and j < len(word):
            if s[i] == word[j]:
                i += 1
                j += 1
            else:
                return False, None
        else:
            if j == len(word):
                return True, i
            else:
                return False, None

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        i = 0
        dp = [0] * (len(s) + 1)
        while i < len(s):
            if i == 0 or dp[i] > 0:
                for word in wordDict:
                    if word[0] == s[i]:
                        equal, j = self.check(s, i, word)
                        if equal:
                            dp[j] += 1
            i += 1
        return dp[-1] != 0
    

print(Solution().wordBreak("cars", ['car', 'ca', 'rs']))
