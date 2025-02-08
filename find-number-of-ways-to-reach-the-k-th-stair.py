from functools import cache


class Solution:
    def waysToReachStair(self, target: int) -> int:
        @cache
        def solve(i, j, k):
            # i is the position
            # j is the jumps
            # k is backtrack
            if i < 0:
                return 0
            if (i - 1) > target:
                return 0
            
            if i == target:
                if k:
                    return 1 + solve(i - 1, j, False) + solve(i + 2**j, j + 1, True)
                else:
                    return 1 + solve(i + 2**j, j + 1, True)
            else:
                if k:
                    return solve(i - 1, j, False) + solve(i + 2**j, j + 1, True)
                else:
                    return solve(i + 2**j, j + 1, True)

        return solve(1, 0, True)


print(Solution().waysToReachStair(524286))
