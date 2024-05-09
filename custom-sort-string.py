from collections import Counter


class Solution:
    def customSortString(self, order: str, s: str) -> str:
        remaining = ""
        f = Counter(s)
        result = ""
        for ch in s:
            if ch not in order:
                remaining += ch
        for ch in order:
            if ch in f:
                result += ch * f[ch]

        return result + remaining


print(Solution().customSortString("bcafg", "abcd"))
