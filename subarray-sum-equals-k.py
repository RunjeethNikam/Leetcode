from typing import List
from collections import defaultdict


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d = defaultdict(int)
        d[0] = 1
        prefix = 0
        result = 0
        for num in nums:
            prefix += num
            if (prefix - k) in d:
                result += d[prefix - k]
            d[prefix] += 1
        return result


print(Solution().subarraySum(nums=[1, 2, 3], k=3))
