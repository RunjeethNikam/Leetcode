from collections import Counter


class Solution:
    def doesAliceWin(self, s: str) -> bool:
        f = Counter(s)
        count = 0
        for ch in ["a", "e", "i", "o", "u"]:
            count += f[ch]
        return count != 0


print(Solution().doesAliceWin("bbcd"))
