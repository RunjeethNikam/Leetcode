from functools import cache


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        @cache
        def solve(i, i1, i2):
            print(i, i1, i2)
            if i == len(s3) and i1 == len(s1) and i2 == len(s2):
                return True
            if i < len(s3) and i1 <= len(s1) and i2 <= len(s2):
                if (
                    i1 < len(s1)
                    and i2 < len(s2)
                    and s3[i] == s1[i1]
                    and s3[i] == s2[i2]
                ):
                    return solve(i + 1, i1 + 1, i2) or solve(i + 1, i1, i2 + 1)
                elif i1 < len(s1) and s3[i] == s1[i1]:
                    return solve(i + 1, i1 + 1, i2)
                elif i2 < len(s2) and s3[i] == s2[i2]:
                    return solve(i + 1, i1, i2 + 1)
            return False

        return solve(0, 0, 0)


print(Solution().isInterleave(s1="aabcc", s2="dbbca", s3="aadbbbaccc"))
