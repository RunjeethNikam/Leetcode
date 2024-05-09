from typing import List
from collections import defaultdict



class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        f = defaultdict(int)
        i = j = result = 0
        while j < len(nums):
            f[nums[j]] += 1
            if f[nums[j]] > k:
                while i <= j and f[nums[j]] > k:
                    f[nums[i]] -= 1
                    i += 1
            result = max(result, j-i + 1)
            j += 1
        return result

print(Solution().maxSubarrayLength([5,5,5,5,5,5,5], 4))
