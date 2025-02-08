from typing import List
from functools import cache


class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        @cache
        def solve(start):
            if start > (len(stoneValue) - 1):
                return 0, 0
            elif start == (len(stoneValue) - 1):
                return stoneValue[start], 0
            else:
                curr_max = float("-inf")
                curr_min = float("inf")
                for i in range(3):
                    mx, mn = solve(start + i + 1)
                    if (sum(stoneValue[start : start + i + 1]) + mn) > curr_max:
                        curr_max = sum(stoneValue[start : start + i + 1]) + mn
                        curr_min = mx
                return curr_max, curr_min

        A, _ = solve(0)
        total = sum(stoneValue)
        B = total - A

        if A == B:
            return "Tie"
        elif A > B:
            return "Alice"
        else:
            return "Bob"


print(Solution().stoneGameIII([-1, -2, -3]))
