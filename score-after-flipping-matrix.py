from typing import List


class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        def flip_row(row):
            for i in range(cols):
                grid[row][i] = 1 - grid[row][i]

        def flip_col(col):
            for r in range(rows):
                grid[r][col] = 1 - grid[r][col]

        for i in range(rows):
            if grid[i][0] == 0:
                flip_row(i)
        for c in range(1, cols):
            zeros = 0
            ones = 0
            for r in range(rows):
                if grid[r][c]:
                    ones += 1
                else:
                    zeros += 1
            if zeros > ones:
                flip_col(c)
        result = 0
        for row in grid:
            binary_string = "".join(map(str, row))
            result += int(binary_string, 2)
        return result


print(Solution().matrixScore([[0]]))
