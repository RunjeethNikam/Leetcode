from typing import List


class Solution:
    def captureForts(self, forts: List[int]) -> int:
        lt = None
        zeros = 0
        captured1 = 0
        for position in forts:
            if position == 0:
                zeros += 1
            else:
                if lt is None:
                    lt = position
                elif lt != position:
                    captured1 = max(captured1, zeros)
                    lt = position
                zeros = 0
        return captured1

print(Solution().captureForts([1,0,0,-1,0,0,-1,0,0,1]))