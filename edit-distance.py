from functools import cache


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @cache
        def solve(i, j):
            if i >= 0 and j >= 0:
                if word1[i] == word2[j]:
                    return solve(i - 1, j - 1)
                else:
                    return (
                        min(
                            solve(i - 1, j),
                            solve(i, j - 1),
                            solve(i - 1, j - 1),
                        )
                        + 1
                    )
            elif i >= 0 or j >= 0:
                return max(i, j) + 1
            else:
                return 0

        return solve(len(word1) - 1, len(word2) - 1)


print(Solution().minDistance(word1="horse", word2="ros"))
