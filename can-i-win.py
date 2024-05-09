from functools import cache


class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        @cache
        def solve(choosableIntegers: int, desiredTotal: int):
            if desiredTotal > 0:
                for chosen in range(1, maxChoosableInteger + 1):
                    msk = 1 << chosen
                    if not (msk & choosableIntegers):
                        choosableIntegers = choosableIntegers ^ msk
                        if chosen >= desiredTotal or not solve(
                            choosableIntegers, desiredTotal - chosen
                        ):
                            return True
                        choosableIntegers = choosableIntegers ^ msk
                return False
            else:
                return True

        if (maxChoosableInteger * (maxChoosableInteger + 1) // 2) < desiredTotal:
            return False
        return solve(0, desiredTotal)


print(Solution().canIWin(5, 50))
