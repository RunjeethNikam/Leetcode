from functools import cache


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @cache
        def solve(i, j):
            if i >= 0 and j >= 0:
                if text1[i] == text2[j]:
                    return solve(i - 1, j - 1) + 1
                else:
                    return max(solve(i - 1, j), solve(i, j - 1))
            return 0

        return solve(len(text1) - 1, len(text2) - 1)


print(Solution().longestCommonSubsequence(text1="abc", text2="def"))
