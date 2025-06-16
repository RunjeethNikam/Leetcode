from typing import List
from functools import cache


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        # values = [r for row in grid for r in row]
        # values.sort()

        def check(i, j):
            return min(i, j) >= 0 and i < rows and j < cols

        def directions(i, j):
            for I, J in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                if check(i + I, j + J):
                    yield i + I, j + J

        visited = set([(0, 0)])

        @cache
        def solve(I, J, mx):
            if I == rows - 1 and J == cols - 1 and grid[I][J] <= mx:
                return True
            for i, j in directions(I, J):
                if (i, j) not in visited and grid[i][j] <= mx:
                    visited.add((i, j))
                    if solve(i, j, mx):
                        visited.remove((i, j))
                        return True
                    visited.remove((i, j))

        low = max(grid[0][0], grid[-1][-1])
        high = max(max(r) for r in grid)
        while low <= high:
            mid = (low + high) // 2
            possible = False
            if grid[0][0] <= mid:
                possible = solve(0, 0, mid)
            if possible:
                high = mid - 1
            else:
                low = mid + 1
        return low


print(
    Solution().swimInWater(
        grid=[
            [26, 99, 80, 1, 89, 86, 54, 90, 47, 87],
            [9, 59, 61, 49, 14, 55, 77, 3, 83, 79],
            [42, 22, 15, 5, 95, 38, 74, 12, 92, 71],
            [58, 40, 64, 62, 24, 85, 30, 6, 96, 52],
            [10, 70, 57, 19, 44, 27, 98, 16, 25, 65],
            [13, 0, 76, 32, 29, 45, 28, 69, 53, 41],
            [18, 8, 21, 67, 46, 36, 56, 50, 51, 72],
            [39, 78, 48, 63, 68, 91, 34, 4, 11, 31],
            [97, 23, 60, 17, 66, 37, 43, 33, 84, 35],
            [75, 88, 82, 20, 7, 73, 2, 94, 93, 81],
        ]
    )
)
