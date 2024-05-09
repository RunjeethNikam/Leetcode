from typing import List


class Solution:
    def canMakeSquare(self, grid: List[List[str]]) -> bool:
        def count(si, ei, sj, ej):
            b = w = 0
            for i in range(si, ei + 1):
                for j in range(sj, ej + 1):
                    if grid[i][j] == "B":
                        b += 1
                    else:
                        w += 1
            return b, w

        # Case 1
        b, w = count(0, 1, 0, 1)
        if b <= 1 or w <= 1:
            return True

        b, w = count(1, 2, 0, 1)
        if b <= 1 or w <= 1:
            return True

        b, w = count(0, 1, 1, 2)
        if b <= 1 or w <= 1:
            return True

        b, w = count(1, 2, 1, 2)
        if b <= 1 or w <= 1:
            return True

        return False


print(Solution().canMakeSquare([["B", "W", "B"], ["W", "B", "W"], ["B", "W", "B"]]))
