from typing import List
from collections import defaultdict


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        dp = defaultdict(int)
        rows = len(matrix)
        cols = len(matrix[0])
        result = 0
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == "1":
                    dp[(i, j)] = (
                        min(dp[(i - 1, j)], dp[(i, j - 1)], dp[(i - 1, j - 1)]) + 1
                    )
                    result = max(result, dp[(i, j)])
        return result * result


print(Solution().maximalSquare(matrix=[["0", "1"], ["1", "0"]]))
