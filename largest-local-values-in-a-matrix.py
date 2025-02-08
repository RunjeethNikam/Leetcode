from typing import List


class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        rows = len(grid)
        cols = len(grid[0])
        result = []

        def mx(i, j):
            mn = float("-inf")
            for r in range(i, i + 3):
                for c in range(j, j + 3):
                    if grid[r][c] > mn:
                        mn = grid[r][c]
            return mn

        for i in range(rows - 2):
            temp = []
            for j in range(cols - 2):
                temp.append(mx(i, j))
            result.append(temp)
        return result


print(
    Solution().largestLocal(
        [
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 2, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
        ]
    )
)
