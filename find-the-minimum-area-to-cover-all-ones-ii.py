from typing import List
from collections import defaultdict


class Solution:
    def minimumSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        dp = defaultdict(lambda: float('inf'))
        for i in range(cols):
            for lenth in range(1, i + 1):
                dp[i][1] 