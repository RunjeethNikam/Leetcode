from typing import List
from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        q = deque()
        count = 0

        def check(i, j):
            return i >= 0 and i < rows and j >= 0 and j < cols

        def adj(i, j):
            d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            for a, b in d:
                if check(i + a, j + b):
                    yield i + a, j + b

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    q.append((i, j, 0))
                elif grid[i][j] == 1:
                    count += 1
        if count == 0:
            return 0
        result = -1
        while q:
            i, j, minutes = q.popleft()
            for I, J in adj(i, j):
                if grid[I][J] == 1:
                    grid[I][J] = 2
                    q.append((I, J, minutes + 1))
                    count -= 1
            result = max(result, minutes)
        if count != 0:
            return -1
        else:
            return result


print(Solution().orangesRotting(grid=[[2, 1, 1], [0, 1, 1], [1, 0, 1]]))
