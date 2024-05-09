from typing import List

class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        lt = None
        mx = 0
        curr = 0
        for num in nums:
            if lt is None:
                if num % 2 == 0 and num <= threshold:
                    lt = num
                    curr = 1
                mx = max(curr, mx)
            elif num <= threshold:
                if num%2 != lt%2:
                    curr += 1
                    lt = num
                elif num%2 == 0:
                    curr = 1
                    lt = num
                else:
                    lt = None
                    curr = 0
                mx = max(curr, mx)        
            else:
                lt = None
                curr = 0
        return mx

print(Solution().longestAlternatingSubarray([2,1,3,1], 1))

