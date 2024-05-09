from typing import List


class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        result = 0
        for i in range(len(nums)):
            mn = nums[i]
            mx = nums[i]
            for j in range(i):
                mn = min(mn, nums[j])
                mx = max(mx, nums[j])
            result += mx-mn
        return result
    

print(Solution().subArrayRanges([1,2,3]))