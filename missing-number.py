from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        N = len(nums)
        sm = sum(nums)
        return (N * (N + 1) // 2) - sm