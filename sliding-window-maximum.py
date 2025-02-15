from typing import List
from collections import defaultdict
from heapq import *


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        h = []
        f = defaultdict(int)
        for i in range(k):
            heappush(h, -nums[i])
            f[nums[i]] += 1
        i = 0
        result = [-h[0]]

        for j in range(k, len(nums)):
            heappush(h, -nums[j])
            f[nums[j]] += 1
            f[nums[i]] -= 1
            i += 1
            while f[-h[0]] <= 0:
                heappop(h)
            result.append(-h[0])
        return result


print(Solution().maxSlidingWindow(nums=[1, 3, 1, 2, 0, 5], k=3))
