from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i+1]:
            i += 1
        
        if i >= 0:
            pass
        



print(Solution().nextPermutation([1, 3, 2]))
