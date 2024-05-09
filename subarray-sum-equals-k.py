from typing import List
from collections import defaultdict


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sm = nums[0]
        d = defaultdict(int)
        d[sm] = 1
        result = 1 if sm == k else 0
        for num in nums[1:]:
            sm += num
            d[sm] += 1
            if (sm - k) in d and k != 0:
                result += d[sm-k]
            elif sm == k:
                result +=  1
        return result
    

print(Solution().subarraySum([1], 0))
print(Solution().subarraySum([1,-1,0], 0))
print(Solution().subarraySum([1,2,3], 3))
print(Solution().subarraySum([-1,-1,1], 0))
