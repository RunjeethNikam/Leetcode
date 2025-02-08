from typing import List
from collections import defaultdict


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        df = defaultdict(int)
        df[0] = 1
        prefix = 0
        result = 0
        for num in nums:
            prefix += num
            if (prefix % k) in df:
                result += df[prefix % k]
            df[prefix % k] += 1
        return result


print(Solution().subarraysDivByK(nums=[-1, -1, -1, -1, -1, -1], k=5))
