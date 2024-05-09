from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if i > 0 or j > 0:
                    left = grid[i][j - 1] if (j - 1) >= 0 else float('inf')
                    top = grid[i - 1][j] if (i - 1) >= 0 else float('inf')
                    grid[i][j] = min(left, top) + grid[i][j]
        return grid[-1][-1]


print(Solution().minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))
