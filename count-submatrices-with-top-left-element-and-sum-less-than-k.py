from typing import List


class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        dp = [[0] * len(grid[0]) for _ in grid]
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                dp[i][j] = grid[i][j]
                if i > 0:
                    dp[i][j] += dp[i - 1][j]
                if j > 0:
                    dp[i][j] += dp[i][j - 1]
                if i > 0 and j > 0:
                    dp[i][j] -= dp[i-1][j - 1]
                if dp[i][j] <= k:
                    count += 1
        return count


print(Solution().countSubmatrices([[7,2,9],[1,5,0],[2,6,6]], 20))
