from typing import List


class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        def solve(arr):
            i = 0
            while i < len(arr):
                if arr[i] == 1:
                    break
                i += 1
            j = len(arr) - 1
            while j >= 0:
                if arr[j] == 1:
                    break
                j -= 1
            return j - i + 1

        r = len(grid)
        c = len(grid[0])
        rows = [0] * r
        cols = [0] * c
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    rows[i] = 1
                    cols[j] = 1
        a = solve(rows)
        b = solve(cols)
        return a * b


print(Solution().minimumArea(grid=[[0, 0], [1, 0]]))
