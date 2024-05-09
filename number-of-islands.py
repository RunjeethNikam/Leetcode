from typing import List


class Solution:
    def dfs(self, i, j, visited, grid):
        if not visited[i][j]:
            visited[i][j] = True
            # top
            if (i - 1) >= 0 and grid[i - 1][j] == "1":
                self.dfs(i - 1, j, visited, grid)
            # down
            if (i + 1) < len(grid) and grid[i + 1][j] == "1":
                self.dfs(i + 1, j, visited, grid)
            # Right
            if (j + 1) < len(grid[0]) and grid[i][j + 1] == "1":
                self.dfs(i, j + 1, visited, grid)
            # Left
            if (j - 1) >= 0 and grid[i][j - 1] == "1":
                self.dfs(i, j - 1, visited, grid)

    def numIslands(self, grid: List[List[str]]) -> int:
        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not visited[i][j] and grid[i][j] == "1":
                    count += 1
                    self.dfs(i, j, visited, grid)
        return count


print(
    Solution().numIslands(
        [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"],
        ]
    )
)
