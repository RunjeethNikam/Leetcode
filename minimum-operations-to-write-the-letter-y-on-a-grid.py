from typing import List
from collections import defaultdict


class Solution:

    def minimumOperationsToWriteY(self, grid: List[List[int]]) -> int:
        def onY(i, j):
            r = len(grid)
            c = len(grid[0])
            if i <= (r // 2):
                return i == j or i == (c - j - 1)
            else:
                return j == c // 2

        f1 = defaultdict(int)
        f2 = defaultdict(int)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if onY(i, j):
                    f1[grid[i][j]] += 1
                else:
                    f2[grid[i][j]] += 1

        mn = float("inf")
        for selected_key in range(3):
            sm = sum([value for k, value in f1.items() if k != selected_key])
            for other_key in range(3):
                if other_key != selected_key:
                    sm2 = sum([value for k, value in f2.items() if k != other_key])
                    mn = min(mn, sm + sm2)

        return mn


print(Solution().minimumOperationsToWriteY([[1, 2, 2], [1, 1, 0], [0, 1, 0]]))
