class Solution:
    def countKeyChanges(self, s: str) -> int:
        s = s.lower()
        count = 0
        i = 1
        while i < len(s):
            if s[i] != s[i-1]:
                count += 1
        return count