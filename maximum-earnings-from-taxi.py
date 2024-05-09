from typing import List
from bisect import *


class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        rides.sort(key=lambda item: (item[1], item[0]))

        dp = [0] * len(rides)
        for index, ride in enumerate(rides):
            start, end, tip = ride
            if index > 0:
                i = bisect(
                    rides, start, hi=index, key=lambda item: item[1]
                )
                dp[index] = max(
                    dp[index - 1], (dp[i - 1] if i > 0 else 0) + end - start + tip
                )
            else:
                dp[index] = end - start + tip
        return dp[-1]


print(
    Solution().maxTaxiEarnings(
        20, [[1, 6, 1], [3, 10, 2], [10, 12, 3], [11, 12, 2], [12, 15, 2], [13, 18, 1]]
    )
)
