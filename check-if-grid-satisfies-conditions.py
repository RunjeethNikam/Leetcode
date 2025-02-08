from typing import List


class Solution:
    def satisfiesConditions(self, grid: List[List[int]]) -> bool:
        rows = len(grid)
        cols = len(grid[0])
        for i in range(rows):
            for j in range(cols):
                right = float("inf")
                if (j + 1) < cols:
                    right = grid[i][j + 1]
                down = grid[i][j]
                if (i + 1) < rows:
                    down = grid[i + 1][j]
                if grid[i][j] != down or grid[i][j] == right:
                    return False
        return True


print(Solution().satisfiesConditions([[1], [2], [3]]))
