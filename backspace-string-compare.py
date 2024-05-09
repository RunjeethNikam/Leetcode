import itertools


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s = list(s)
        t = list(t)
        i = j = 0
        while j < len(s):
            if s[j] == '#':
                i = max(0, i-1)
            else:
                s[i] = s[j]
                i += 1
            j += 1
        s = ''.join(s[:i])

        i = j = 0
        while j < len(t):
            if t[j] == '#':
                i = max(0, i-1)
            else:
                t[i] = t[j]
                i += 1
            j += 1
        t = ''.join(t[:i])
        return s == t
print(
    Solution().backspaceCompare("y#fo##f", "y#f#o##f")
)
