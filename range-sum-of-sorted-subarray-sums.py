from typing import List
from heapq import *


class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        sm = 0
        min_heap = []
        for i, value in enumerate(nums):
            sm += value
            temp = sm
            # heappush(min_heap, temp)
            for j in range(i):
                heappush(min_heap, temp)
                temp -= nums[j]
                # heappush(min_heap, temp)
            heappush(min_heap, temp)
        print(sorted(min_heap))
        i = 1
        sum = 0
        while i <= right:
            item = heappop(min_heap)
            if i >= left:
                sum += item
            i += 1
        return sum


print(Solution().rangeSum(nums = [1,2,3,4], n = 4, left = 1, right = 10))
