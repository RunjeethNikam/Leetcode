from collections import Counter
from string import ascii_lowercase



class Solution:
    def minimizeStringValue(self, s: str) -> str:
        s = list(s)
        f = Counter(s) 
        result = []
        if '?' in f:
            for index, value in enumerate(s):
                if value == '?':
                    mn_ch = None
                    mn_f = float('inf')
                    for ch in ascii_lowercase:
                        if f.get(ch, 0) < mn_f:
                            mn_f = min(mn_f, f[ch])
                            mn_ch = ch
                    result.append(mn_ch)
                    f[mn_ch] += 1
        result.sort()
        i = 0
        for index, value in enumerate(s):
                if value == '?':
                     s[index] = result[i]
                     i += 1
                     
        return "".join(s)
    
print(Solution().minimizeStringValue("abcdefghijklmnopqrstuvwxy??"))
                