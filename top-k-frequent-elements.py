from typing import List
from collections import Counter
from heapq import *


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = [[] for _ in range(100000)]
        c = Counter(nums)
        for key, value in c.items():
            h[value].append(key)
        result = []
        for value in reversed(h):
            if len(value) != 0:
                k -= len(value)
                result.extend(value)
            if k == 0:
                break
        return result


print(Solution().topKFrequent(nums=[1, 1, 1, 2, 2, 3], k=2))
