from typing import List
from collections import defaultdict


class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        dp = defaultdict(lambda: defaultdict(int))
        dp_count = defaultdict(int)
        nums.sort()
        for i, num in enumerate(nums):
            left = num - k
            for j, item in enumerate(nums[:i]):
                if item == left:
                    continue
                


print(Solution().beautifulSubsets(nums=[4, 2, 5, 9, 10, 3], k=1))
