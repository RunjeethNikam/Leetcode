from collections import defaultdict, Counter
from typing import List
from math import *


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        d = defaultdict(set)
        for i, num in enumerate(nums):
            for j in range(i):
                I, J = nums[i], nums[j]
                gc = gcd(I,J)
                if I % J == 0:
                    d[gc].add(J)
                    d[gc].add(I)
        return list(max(d.values(), key=len))
    

print(Solution().largestDivisibleSubset([1,2,4,8]))
