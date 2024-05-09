from typing import List


class Solution:

    def get_item(self, nums, index):
        if index < 0:
            return float('inf')
        try:
            return nums[index]
        except IndexError:
            return float('inf')

    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if nums[0] < nums[-1]:
            return nums[0]

        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[start] <= nums[end]:
                return nums[start]
            if self.get_item(nums, mid-1) > self.get_item(nums, mid) < self.get_item(nums, mid+1):
                return nums[mid]
            elif nums[start] <= nums[mid]:
                start = mid + 1
            else:
                end = mid - 1

print(Solution().findMin([2,3,4,5,1]))
print(Solution().findMin([3,4,5,1,2]))
print(Solution().findMin([2,1]))
print(Solution().findMin([4,5,6,7,0,1,2]))
print(Solution().findMin([11,13,15,17]))