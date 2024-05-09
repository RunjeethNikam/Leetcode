from collections import Counter


class Solution:
    def lastNonEmptyString(self, s: str) -> str:
        f = Counter(s)
        max_f = max(f.values())
        if max_f == 1:
            return s
        for key in f.keys():
            if f[key] < max_f:
                f[key] = 0

        result = ''
        for ch in s[::-1]:
            if f[ch] > 0:
                result += ch
                f[ch] = 0
        
        return result[::-1]
    
print(Solution().lastNonEmptyString("abcd"))
