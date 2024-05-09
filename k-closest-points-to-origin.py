from typing import List
from math import sqrt
from heapq import heappush, heappop


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = []
        for x, y in points:
            dist = sqrt(x**2 + y**2)
            heappush(h, (-dist, x, y))
            if len(h) > k:
                heappop(h)
        return list(map(lambda item: [item[1], item[2]], h))


print(Solution().kClosest([[3, 3], [5, -1], [-2, 4]], 2))
