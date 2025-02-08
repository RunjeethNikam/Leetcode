from functools import cache

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:

        @cache
        def solve(start, end):
            if start == end:
                return 1
            elif start < end:
                if s[start] == s[end]:
                    return 2 + solve(start + 1, end - 1)
                else:
                    return max(solve(start + 1, end), solve(start, end - 1))
            return 0

        start = 0
        end = len(s) - 1
        return solve(start, end)


print(Solution().longestPalindromeSubseq("cbbd"))
