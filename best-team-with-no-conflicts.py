from typing import List


class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        c = list(zip(ages, scores))
        c.sort()
        dp = map(lambda t: t[-1], c)
        for i in range(len(c)):
            for j in range(i):
                if c[i][1] >= c[j][1] or c[i][0] == c[j][0]:
                    dp[i] = max(dp[i], c[i][1] + dp[j])
        return max(dp)


print(
    Solution().bestTeamScore(
        scores=[1, 3, 7, 3, 2, 4, 10, 7, 5], ages=[4, 5, 2, 1, 1, 2, 4, 1, 4]
    )
)
