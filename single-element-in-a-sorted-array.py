from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        if nums[0] != nums[1]:
            return nums[0]

        if nums[-1] != nums[-2]:
            return nums[-1]

        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] != nums[mid-1] and nums[mid] != nums[mid+1]:
                return nums[mid]
            if nums[mid] == nums[mid-1]:
                mid -= 1

            right = high - mid + 1
            if right % 2 == 0:
                high = mid - 1
            else:
                low = mid + 2


print(Solution().singleNonDuplicate(nums=[1, 1, 3, 3, 5, 5, 7, 7, 8, 11, 11]))
