from typing import List
from collections import defaultdict


class Solution:
    def shortestDistanceAfterQueries(
        self, n: int, queries: List[List[int]]
    ) -> List[int]:
        dp = defaultdict(int)
        for i in range(n):
            dp[i] = n-i-1
        result = []
        for u, v in queries:
            dp[u] = min(dp[u], dp[v]+1)
            for j in range(u-1, -1, -1):
                dp[j] = min(dp[j], 1 + dp[j + 1])
            result.append(dp[0])
        # dp = defaultdict(lambda: (0, 0))
        # for i in range(n):
        #     dp[i] = (i, n - i - 1)
        # result = []
        # for u, v in queries:
        #     v_zero, v_one = dp[v]
        #     u_zero, u_one = dp[u]
        #     dp[u] = (u_zero, min(1 + v_one, u_one))
        #     dp[v] = (min(v_zero, 1 + u_zero), v_one)
        #     result.append(sum(dp[u]))
        return result

# 4,3
print(Solution().shortestDistanceAfterQueries(n=6, queries=[[1,3],[3,5]]))
