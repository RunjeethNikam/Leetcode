from typing import List
from queue import Queue


class Solution:

    def maxSubarray(self, nums):
        max_sm = float('-inf')
        current_sm = 0
        for num in nums:
            current_sm += num
            if current_sm > max_sm:
                max_sm = current_sm
            if current_sm < 0:
                current_sm = 0
        return max_sm
    
    def minSubarray(self, nums):
        min_sm = float('inf')
        current_sm = 0
        for num in nums:
            current_sm += num
            if current_sm < min_sm:
                min_sm = current_sm
            if current_sm > 0:
                current_sm = 0
        return min_sm


    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        sm = sum(nums)
        normal_sm = self.maxSubarray(nums)
        special_sm = self.minSubarray(nums)
        print(sm, normal_sm, special_sm)
        if special_sm == sm:
            return normal_sm
        else:
            return max(normal_sm, sm-special_sm)
    
print(Solution().maxSubarraySumCircular([5,-3,5]))
