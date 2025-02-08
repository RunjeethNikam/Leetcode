from collections import Counter, defaultdict
import string
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_f = Counter(p)
        f = defaultdict(int)
        l = 0
        result = []
        for index, ch in enumerate(s):
            f[ch] += 1
            while index - l + 1 > len(p):
                f[s[l]] -= 1
                l += 1
            if index - l + 1 == len(p):
                if all([p_f[ch] == f[ch] for ch in string.ascii_lowercase]):
                    result.append(l)
        return result


print(Solution().findAnagrams(s = "abab", p = "ab"))
