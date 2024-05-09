from typing import List

class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        result = nums[0]
        min1 = min(nums[1], nums[2])
        min2 = max(nums[1], nums[2])
        for i in range(3, len(nums)):
            if nums[i] < min1:
                min2 = min1
                min1 = nums[i]
            elif nums[i] < min2:
                min2 = nums[i]
        return result + min1 + min2

print(Solution().minimumCost([1,1,1,1]))