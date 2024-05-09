from collections import defaultdict



class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        f = defaultdict(int)
        i = 0
        result = 0
        for index, ch in enumerate(s):
            f[ch] += 1
            if f[ch] == 3:
                while f[ch] == 3:
                    f[s[i]] -= 1
                    i += 1
            result = max(result,index - i + 1)
        return result
    

print(Solution().maximumLengthSubstring("abcdea"))