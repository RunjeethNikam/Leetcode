from typing import List
from bisect import *


class Solution:
    def jobScheduling(
        self, startTime: List[int], endTime: List[int], profit: List[int]
    ) -> int:
        intervals = list(zip(startTime, endTime, profit))
        intervals.sort(key=lambda interval: (interval[1], interval[0]))
        dp = []
        for s, e, p in intervals:
            if not dp:
                dp.append((e, p))
            else:
                i = bisect(dp, s, key=lambda item: item[0])
                if i > 0:
                    if dp[-1][-1] > (p + dp[i - 1][1]):
                        dp.append((e, dp[-1][-1]))
                    else:
                        dp.append((e, p + dp[i - 1][1]))
                else:
                    if p > dp[-1][-1]:
                        dp.append((e, p))
                    else:
                        dp.append((e, dp[-1][-1]))
        return max(dp, key=lambda item: item[1])[1]


print(
    Solution().jobScheduling(
        startTime=[4, 2, 4, 8, 2], endTime=[5, 5, 5, 10, 8], profit=[1, 2, 8, 10, 4]
    )
)
