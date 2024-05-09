from typing import List
from collections import deque


class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        result = []

        def solve(i, j):
            q = deque([[i, j, 0]])
            x, y = i, j
            direction = [[1, 0], [0, 1], [-1, 0], [0, -1]]
            while q:
                i, j, d = q.popleft()
                land[i][j] = 0
                for index, [a, b] in enumerate(direction):
                    I = i + a
                    J = j + b
                    if (
                        I >= 0
                        and I < len(land)
                        and J >= 0
                        and J < len(land[0])
                        and land[I][J] == 1
                    ):
                        q.append([I, J, index])
                    if (
                        I >= 0
                        and I < len(land)
                        and J >= 0
                        and J < len(land[0])
                        and land[I][J] == 1
                    ):
                        land[I][J] = 0
                    if d == 1 or d == 0:
                        x, y = i, j
            return x, y

        for i in range(len(land)):
            for j in range(len(land[0])):
                if land[i][j] == 1:
                    a = i
                    b = j
                    c, d = solve(i, j)
                    result.append([a, b, c, d])
        return result


print(Solution().findFarmland([[0, 1], [0, 1]]))
