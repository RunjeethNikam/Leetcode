from typing import List
from collections import Counter



class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        f = Counter(nums)
        count = 0
        for key in f.keys():
            r = k - key
            if key == r:
                count += (f[key] // 2)
                f[key] = f[key] % 2
            elif r in f:
                m = min(f[r], f[key])
                count += m
                f[r] -= m
                f[key] -= m

        return  count
    
print(Solution().maxOperations([1,2,2,3], 4))