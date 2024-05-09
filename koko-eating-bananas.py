import math

from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def check(k):
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / k)
            return hours <= h

        low = 1
        high = max(piles)
        while low <= high:
            mid = (high + low) // 2
            if check(mid):
                high = mid - 1
            else:
                low = mid + 1
        return low

print(Solution().minEatingSpeed([30,11,23,4,20], 6))
