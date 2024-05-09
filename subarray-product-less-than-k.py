from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        i = 0
        j = 0
        p = 1
        result = 0
        while j < len(nums):
            p *= nums[j]
            if p >= k:
                while i <= j and p >= k:
                    p /= nums[i]
                    i += 1
            result += (j - i + 1)
            j += 1
        return result
    
print(Solution().numSubarrayProductLessThanK([1,2,3], 0))
            