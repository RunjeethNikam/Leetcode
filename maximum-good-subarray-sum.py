from typing import List


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        d = {}
        sm = 0
        result = float('-inf')
        for num in nums:
            if num in d:
                d[num] = min(sm, d[num])
            else:
                d[num] = sm
            sm += num
            if (num-k) in d:
                result = max(result, sm - d[num-k])
            elif (num + k) in d:
                result = max(result, sm - d[num + k])
        return result 

print(Solution().maximumSubarraySum([-1,3,2,4,5], 3))
