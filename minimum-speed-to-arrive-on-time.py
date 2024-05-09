from typing import List
import math


class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:

        def check(r):
            result = 0
            for index, d in enumerate(dist):
                if index != (len(dist) - 1):
                    result += math.ceil(d / r)
                else:
                    result += d / r
            return result

        low = 1
        high = 1000000000
        # if ((len(dist) - 1) > hour) or (hour > check(low)):
        #     return -1
        while low <= high:
            mid = (high + low) // 2
            t = check(mid)
            if t <= hour:
                high = mid - 1
            else:
                low = mid + 1
        print(round(check(low), 2), round(hour, 2))
        return low if round(check(low), 2) <= round(hour, 2) else -1


# print(Solution().minSpeedOnTime([1, 1, 100000], 2.01))
print(Solution().minSpeedOnTime([1, 3, 2], 6))
# print(Solution().minSpeedOnTime([1, 3, 2], 2.7))
# print(Solution().minSpeedOnTime([1, 3, 2], 1.9))
# print(Solution().minSpeedOnTime([2,1,5,4,4,3,2,9,2,10], 75.12))
