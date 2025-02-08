from typing import List
from collections import defaultdict


class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        moves, flag = 0,0
        nums.sort()
        for num in nums:
            flag = max(num, flag)
            moves += (flag - num)
            flag += 1
        return moves


print(Solution().minIncrementForUnique(nums=[3, 2, 1, 2, 1, 7]))
