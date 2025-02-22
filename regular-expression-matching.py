from functools import cache
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
        @cache
        def solve(i, j):
            if i < len(s) and j < len(p):
                if s[i] == p[j]:
                    if (j + 1) < len(p) and p[j + 1] == "*":
                        return solve(i + 1, j) or solve(i + 1, j + 2) or solve(i, j + 2)
                    else:
                        return solve(i + 1, j + 1)
                if p[j] == ".":
                    if (j + 1) < len(p) and p[j + 1] == "*":
                        return solve(i + 1, j) or solve(i + 1, j + 2) or solve(i, j + 2)
                    else:
                        return solve(i + 1, j + 1)
                if s[i] != p[j] and (j + 1) < len(p) and p[j + 1] == "*":
                    return solve(i, j + 2)

            if i == len(s) and j == len(p):
                return True
            if j + 1 < len(p) and p[j + 1] == "*":
                return solve(i, j + 2)
            return False

        return solve(0, 0)


print(Solution().isMatch(s="bbbba", p=".*a*a"))
