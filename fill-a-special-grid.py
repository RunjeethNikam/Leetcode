from typing import List


class Solution:
    def specialGrid(self, n: int) -> List[List[int]]:
        rows = 2**n
        cols = 2**n
        grid = [[0] * cols for _ in range(rows)]

        def solve(start_row, start_col, lenght, start_val):
            print(start_row, start_col, lenght, start_val)
            if lenght == 1:
                grid[start_row][start_col] = start_val
                return
            else:
                new_length = lenght // 2
                count = (lenght * lenght) // 4
                solve(
                    start_row,
                    start_col,
                    new_length,
                    start_val + 3 * (count),
                )
                solve(
                    start_row,
                    start_col + new_length,
                    new_length,
                    start_val,
                )
                solve(
                    start_row + new_length,
                    start_col + new_length,
                    new_length,
                    start_val + count,
                )
                solve(
                    start_row + new_length,
                    start_col,
                    new_length,
                    start_val + 2 * (count),
                )

        solve(0, 0, 2**n, 0)
        return grid


print(Solution().specialGrid(2))
