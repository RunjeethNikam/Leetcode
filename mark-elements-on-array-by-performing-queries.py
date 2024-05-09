from typing import List
from heapq import heapify, heappush, heappop


class Solution:
    def unmarkedSumArray(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        h = []
        for index, num in enumerate(nums):
            heappush(h, (num, index))

        mark = [False] * len(nums)
        sm = sum(nums)

        result = []
        for i, k in queries:
            if not mark[i]:
                sm -= nums[i]
                mark[i] = True
            while k and h:
                num, index = heappop(h)
                if not mark[index]:
                    mark[index] = True
                    sm -= num
                    k -= 1
                else:
                    pass
            result.append(sm)

        return result
    
print(Solution().unmarkedSumArray([1,4,2,3], [[0,1]]))