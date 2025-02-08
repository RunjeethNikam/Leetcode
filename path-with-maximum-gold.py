from typing import List


class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        mx = 0

        def adj(i, j):
            direction = [(i + 0, j + 1), (i + 0, j - 1), (i + 1, j + 0), (i - 1, j + 0)]
            for ai, aj in direction:
                if min(ai, aj) >= 0 and ai < rows and aj < cols and grid[ai][aj] != 0:
                    yield (ai, aj)

        def dfs(i, j, visited: set):
            mx = 0
            for ai, aj in adj(i, j):
                if (ai, aj) not in visited:
                    visited.add((ai, aj))
                    mx = max(mx, grid[ai][aj] + dfs(ai, aj, visited))
                    visited.remove((ai, aj))
            return mx

        visited = set()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] != 0:
                    visited.add((i, j))
                    mx = max(mx, grid[i][j] + dfs(i, j, visited))
                    visited.remove((i, j))
        return mx


print(Solution().getMaximumGold([[0, 6, 0], [5, 8, 7], [0, 9, 0]]))
