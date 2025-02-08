from typing import List
from heapq import *
from collections import defaultdict


class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:

        def solve(day):
            count = 0
            b = 0
            for d in bloomDay:
                if d > day:
                    b += count // k
                    count = 0
                else:
                    count += 1
            b += count // k
            return b >= m

        if m * k > len(bloomDay):
            return -1

        low = min(bloomDay)
        high = max(bloomDay)
        result = None
        while low <= high:
            mid = (low + high) // 2
            if solve(mid):
                high = mid - 1
                result = mid
            else:
                low = mid + 1

        return result


print(Solution().minDays(bloomDay=[1, 10, 3, 10, 2], m=3, k=1))
