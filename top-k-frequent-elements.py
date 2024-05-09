from typing import List
from collections import Counter
from heapq import *


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = []
        c = Counter(nums)
        for key, value in c.items():
            heappush(h, (-value, key))
            if len(h) > k:
                heappop(h)
        return list(map(lambda item: item[1], h))


print(Solution().topKFrequent([1,1,1,2,2,3], k = 2))
