from typing import List
from heapq import *


class Solution:
    def minimumCost(
        self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]
    ) -> int:
        h = []  # max heap
        number_of_vertical_cuts = 0
        number_of_horizontal_cuts = 0
        for index in horizontalCut:
            heappush(h, (-index, True))
        for index in verticalCut:
            heappush(h, (-index, False))
        result = 0
        while h:
            index, is_horizontal = heappop(h)
            index = -index
            if is_horizontal:
                result += index * (number_of_vertical_cuts + 1)
                number_of_horizontal_cuts += 1
            else:
                result += index * (number_of_horizontal_cuts + 1)
                number_of_vertical_cuts += 1
        return result


print(Solution().minimumCost(m=2, n=2, horizontalCut=[7], verticalCut=[4]))
