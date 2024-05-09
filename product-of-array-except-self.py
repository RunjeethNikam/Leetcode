from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        curr = 1
        i = 0
        while i < len(nums):
            result[i] = result[i]  * curr
            curr *= nums[i]
            i += 1

        curr = 1
        i = len(nums)-1
        while i >= 0:
            result[i] = result[i]  * curr
            curr *= nums[i]
            i -= 1

        return result
        
        

Solution().productExceptSelf([1,2,3,4])