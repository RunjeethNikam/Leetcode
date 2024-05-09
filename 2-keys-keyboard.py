from functools import lru_cache


class Solution:
    def minSteps(self, n: int) -> int:
        @lru_cache(None)
        def solve(a, c):
            if a == n:
                return 0
            if a > n:
                return float('inf')
            left = float('inf')
            if a != c:
                left = solve(a, a)
            right = float('inf')
            if c != 0:
                right = solve(a + c, c)
            return min(left, right) + 1
        return solve(1, 0)
    

print(Solution().minSteps(9))
        