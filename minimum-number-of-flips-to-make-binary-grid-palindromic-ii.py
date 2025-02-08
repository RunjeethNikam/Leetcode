from typing import List


class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        ones = 0
        for row in grid:
            ones += sum(row)
        rows = len(grid)
        cols = len(grid[0])
        for i in range(rows):
            for j in range(cols):
                a, b, c, d = (
                    grid[i][j],
                    grid[i][cols - 1 - j],
                    grid[rows - 1 - i][cols - 1 - j],
                    grid[rows - 1 - i][j],
                )
                current_ones = a + b + c + d
                current_zeros = 4 - current_ones
                if (current_zeros + ones) % 4 == 0:
                    mn = current_zeros
                
