from typing import List
from heapq import *


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        visited = set()
        rows = len(matrix)
        cols = len(matrix[0])
        h = [(matrix[0][0], 0, 0)]
        for smallest in range(k):
            value, i, j = heappop(h)
            if k - 1 == smallest:
                return value
            # bottom
            if (i + 1, j) not in visited and i + 1 < rows:
                heappush(h, (matrix[i + 1][j], i + 1, j))
                visited.add((i + 1, j))

            # right
            if (i, j + 1) not in visited and j + 1 < cols:
                heappush(h, (matrix[i][j + 1], i, j + 1))
                visited.add((i, j + 1))


print(Solution().kthSmallest(matrix=[[-5]], k=1))
