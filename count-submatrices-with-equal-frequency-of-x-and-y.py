from collections import defaultdict
from typing import List


class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        freq = defaultdict(lambda: (0, 0))  # x,y
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                top = freq[(i - 1, j)]
                left = freq[(i, j - 1)]
                d = freq[(i - 1, j - 1)]
                c_x, c_y = 0, 0
                if grid[i][j] == "X":
                    c_x += 1
                elif grid[i][j] == "Y":
                    c_y += 1
                freq[(i, j)] = (
                    top[0] + left[0] - d[0] + c_x,
                    top[1] + left[1] - d[1] + c_y,
                )
        count = 0
        for key, (x, y) in freq.items():
            if x == y and x >= 1:
                count += 1
        return count


print(Solution().numberOfSubmatrices(grid = [[".","."],[".","."]]))
