from collections import defaultdict
from typing import *


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        if len(nums) == 2:
            return nums
        dp = defaultdict(int)
        xor = 0
        for num in nums:
            xor ^= num 
            for place in range(32):
                msk = 1 << place
                if msk & num:
                    dp[place] ^= num
        result = []
        for place in range(32):
            msk = 1 << place
            if msk & xor:
                value = dp[place]
                if value in nums and (xor ^ value) in nums:
                    return [value, xor ^ value]
    
print(Solution().singleNumber([0,1,1,2]))