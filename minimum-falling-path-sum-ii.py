from typing import List


class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        def get_min(i, j):
            if i - 1 >= 0:
                return min(value for index, value in enumerate(dp[i - 1]) if index != j)
            else:
                return 0

        dp = [[0] * len(grid[0]) for _ in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                dp[i][j] = grid[i][j] + get_min(i, j)
        return min(dp[-1])


print(Solution().minFallingPathSum([[7]]))
