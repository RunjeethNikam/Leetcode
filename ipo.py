from typing import List
from heapq import heappush, heappop


class Solution:
    def findMaximizedCapital(
        self, k: int, w: int, profits: List[int], capital: List[int]
    ) -> int:
        mnh = []
        mxh = []
        result = 0
        for p, c in zip(profits, capital):
            heappush(mnh, (c, p))
        while k > 0:
            while mnh and mnh[0][0] <= w:
                c, p = heappop(mnh)
                heappush(mxh, (-p, c))

            if mxh:
                top = heappop(mxh)
                result += -top[0]
                w += -top[0]
                k -= 1
            else:
                return w
        return w


print(Solution().findMaximizedCapital(1, 2, [1, 2, 3], [1, 1, 2]))
