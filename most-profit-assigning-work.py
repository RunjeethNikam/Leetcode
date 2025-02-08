from typing import List
from bisect import *


class Solution:
    def maxProfitAssignment(
        self, difficulty: List[int], profit: List[int], worker: List[int]
    ) -> int:
        dp = list(zip(difficulty, profit))
        dp.sort()
        mx = [dp[0][1]]
        for i in range(1, len(dp)):
            mx.append(max(mx[-1], dp[i][1]))
        result = 0
        for w in worker:
            index = bisect_right(dp, w, key=lambda item: item[0])
            if index > 0:
                result += mx[index - 1]
        return result


print(
    Solution().maxProfitAssignment(
        difficulty=[2, 4, 6, 8, 10], profit=[10, 20, 30, 40, 50], worker=[1, 5, 6, 7]
    )
)
