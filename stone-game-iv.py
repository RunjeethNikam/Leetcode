from math import *
from functools import cache


class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        @cache
        def solve(n: int):
            if n > 0:
                for option in range(1, n + 1):
                    if option * option > n:
                        break
                    if not solve(n - option * option):
                        return True
                return False
            else:
                return False

        return solve(n)


print(Solution().winnerSquareGame(4))
