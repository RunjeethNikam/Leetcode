from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        prefix = []
        mn = float("inf")
        for index, num in enumerate(nums):
            prefix.append(min(num, mn))
            mn = prefix[-1]

        suffix = [None] * len(nums)
        mx = float("-inf")
        index = len(nums) - 1
        while index >= 0:
            value = nums[index]
            suffix[index] = max(mx, value)
            mx = suffix[index]
            index -= 1

        for i in range(1, len(nums)-1):
            if prefix[i-1] < nums[i] and nums[i] < suffix[i+1]:
                return True

        return False


print(Solution().increasingTriplet([2,1,5,0,4,6]))
