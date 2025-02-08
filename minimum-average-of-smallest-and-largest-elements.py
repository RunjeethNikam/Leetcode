from typing import List


class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        i = 0
        j = len(nums) - 1
        mn = float("inf")
        while i < j:
            mn = min(mn, (nums[i] + nums[j]) / 2)
            i += 1
            j -= 1
        return mn


print(Solution().minimumAverage(nums = [1,9,8,3,10,5]))
