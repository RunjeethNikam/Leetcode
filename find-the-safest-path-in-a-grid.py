from typing import List
from collections import deque, defaultdict
from heapq import *


class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        N = len(grid)
        dist = defaultdict(int)

        def in_bound(i, j):
            return min(i, j) >= 0 and max(i, j) < N

        def adj(i, j):
            return [
                (i + 1, j),
                (i - 1, j),
                (i, j + 1),
                (i, j - 1),
            ]

        def dfs():
            while q:
                i, j = q.popleft()
                d = dist[(i, j)]
                for I, J in adj(i, j):
                    if (I, J) not in dist and in_bound(I, J):
                        q.append((I, J))
                        dist[(I, J)] = d + 1

        q = deque()
        for i in range(N):
            for j in range(N):
                if grid[i][j] == 1:
                    dist[(i, j)] = 0
                    q.append((i, j))

        dfs()

        h = [(-dist[(0, 0)], 0, 0, 0)]
        visited = set()
        while h:
            d, i, j = heappop(h)
            d = -d
            if (i, j) == (N - 1, N - 1):
                return d
            for I, J in adj(i, j):
                if (I, J) not in visited and in_bound(I, J):
                    visited.add((I, J))
                    heappush(h, (-min(d, dist[(I, J)]), I, J))


print(Solution().maximumSafenessFactor(grid=[[1, 0, 0], [0, 0, 0], [0, 0, 1]]))
