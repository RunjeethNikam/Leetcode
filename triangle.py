from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = triangle[0]
        for i in range(1, len(triangle)):
            for j in range(len(triangle[i])):
                triangle[i][j] = min(
                    triangle[i][j] + (dp[j - 1] if (j - 1) > -1 else float('inf')),
                    triangle[i][j] + (dp[j] if (j) < len(dp) else float('inf')),
                )
            dp = triangle[i]
        return min(dp[-1])


print(Solution().minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))
