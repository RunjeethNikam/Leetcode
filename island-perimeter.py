from typing import List


class Solution:

    def islandPerimeter(self, grid: List[List[int]]) -> int:
        direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        count = 0

        rows = len(grid)
        cols = len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]:
                    count += 4
                    for r, c in direction:
                        R = i + r
                        C = j + c
                        if (
                            R >= 0
                            and R < rows
                            and C >= 0
                            and C < cols
                            and grid[R][C] == 1
                        ):
                            count -= 1

        return count


print(
    Solution().islandPerimeter([[1]])
)
