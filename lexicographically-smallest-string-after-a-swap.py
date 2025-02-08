class Solution:
    def getSmallestString(self, s: str) -> str:
        s = list(s)
        for i in range(1, len(s)):
            if int(s[i - 1]) % 2 == int(s[i]) % 2 and s[i - 1] > s[i]:
                s[i - 1], s[i] = s[i], s[i - 1]
                break
        return "".join(s)


print(Solution().getSmallestString("001"))
