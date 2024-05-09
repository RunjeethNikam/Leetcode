from typing import List
from collections import deque


class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:

        def check(i,j):
            return i >= 0 and i< len(grid) and j>= 0 and j < len(grid[0])

        def dfs(q: deque, visited: set):
            direction = [
                [-1, 0],
                [0, 1],
                [1, 0],
                [0, -1]
            ]
            while len(q) != 0:
                i, j, d = q.popleft()
                if grid[i][j] != 1:
                    grid[i][j] = d
                for R, C in direction:
                    if (i+R, j + C) not in visited and check(i+R, j+C):
                        visited.add((i+R, j + C))
                        q.append((i+R, j + C, d + 1))

        visited = set()
        q = deque()
        one = False
        zero = False
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    one = True
                    q.append((i, j, 0))
                    visited.add((i, j))
                else:
                    zero = True
        
        if len(q) == 0:
            return -1

        dfs(q, visited)

        mx = float('-inf')
        for i in grid:
            for j in i:
                mx = max(mx, j)
        return mx if one and zero else -1


print(Solution().maxDistance([[1, 0, 0], [0, 0, 0], [0, 0, 0]]))


# from typing import List
# from collections import deque


# class Solution:
#     def maxDistance(self, grid: List[List[int]]) -> int:

#         def check(i, j):
#             return i >= 0 and j >= 0 and i < len(grid) and j < len(grid[0])

#         def bfs(q, visited):
#             directions = [
#                 (0, 1, 1),
#                 (-1, 0, 1),
#                 (1, 0, 1),
#                 (0, -1, 1),
#             ]
#             while len(q) != 0:
#                 i, j, distance = q.popleft()
#                 grid[i][j] = distance
#                 for I, J, D in directions:
#                     if check(i + I, j + J) and (i + I, j + J) not in visited:
#                         visited.add((i+I, j+J))
#                         q.append((i + I, j + J, distance + D))

#         q = deque()
#         visited = set()
#         for i in range(len(grid)):
#             for j in range(len(grid[0])):
#                 if grid[i][j] == 1:
#                     q.append((i, j, 0))
#                     visited.add((i, j))
#         bfs(q, visited)

#         mx = float("-inf")
#         for v1 in grid:
#             for v2 in v1:
#                 mx = max(mx, v2)
#         if mx == float("inf") or mx == 0:
#             return -1
#         return mx


# print(
#     Solution().maxDistance(
#         [
#             [1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
#             [1, 1, 0, 1, 1, 1, 0, 1, 1, 0],
#             [0, 1, 1, 0, 1, 0, 0, 1, 0, 0],
#             [1, 0, 1, 0, 1, 0, 0, 0, 0, 0],
#             [0, 1, 0, 0, 0, 1, 1, 0, 1, 1],
#             [0, 0, 1, 0, 0, 1, 0, 1, 0, 1],
#             [0, 0, 0, 1, 1, 1, 1, 0, 0, 1],
#             [0, 1, 0, 0, 1, 0, 0, 1, 0, 0],
#             [0, 0, 0, 0, 0, 1, 1, 1, 0, 0],
#             [1, 1, 0, 1, 1, 1, 1, 1, 0, 0],
#         ]
#     )
# )
