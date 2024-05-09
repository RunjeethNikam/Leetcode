from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_so_far = float('-inf')
        current_max = 0
        for num in nums:
            current_max += num
            if current_max > max_so_far:
                max_so_far = current_max
            if max_so_far < 0:
                max_so_far = 0
        return max_so_far