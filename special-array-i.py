from typing import *

class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        last = nums[0] % 2
        for i in range(1, len(nums)):
            if last == nums[i] % 2:
                return False
            last = nums[i] % 2
        return True

print(Solution().isArraySpecial([4,3,1,6]))
