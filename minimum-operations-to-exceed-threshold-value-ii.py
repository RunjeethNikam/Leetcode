from heapq import heapify, heappop, heappush
from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapify(nums)
        count = 0
        while len(nums) > 1:
            a = heappop(nums)
            b = heappop(nums)
            if a >= k and b >= k:
                break
            else:
                heappush(nums, min(a, b) * 2 + max(a, b))
        return count