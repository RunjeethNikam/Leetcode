from typing import List
from pprint import pprint


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        directions = [(+1, 0), (-1, 0), (0, +1), (0, -1)]

        def dfs(i, j):
            result = 0
            if i >= 0 and i < rows and j >= 0 and j < cols and grid[i][j]:
                result += 1
                grid[i][j] = 0
                for I, J in directions:
                    result += dfs(i + I, j + J)
            return result

        result = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] != 0:
                    result = max(result, dfs(i, j))
        return result


print(Solution().maxAreaOfIsland(grid=[[0, 0, 0, 0, 0, 0, 0, 0]]))
