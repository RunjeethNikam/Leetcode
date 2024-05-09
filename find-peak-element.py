from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        def solve(nums, left, right):
            while left < right:
                mid = (left + right) // 2
                if (
                    nums[mid] > nums[mid + 1]
                    and (mid - 1 >= 0)
                    and nums[mid] > nums[mid - 1]
                ):
                    return mid
                elif nums[mid] < nums[mid + 1]:
                    left = mid + 1
                else:
                    right = mid - 1
            return left

        return solve(nums, 0, len(nums) - 1)


print(Solution().findPeakElement([1, 2, 1]))


# class Solution:

#     def get_item(self, nums, i):
#         if i < 0:
#             return float("-inf")
#         else:
#             try:
#                 return nums[i]
#             except IndexError:
#                 return float("-inf")

#     def findPeakElement(self, nums: List[int]) -> int:
#         start = 0
#         end = len(nums) - 1
#         while start <= end:
#             mid = (start + end) // 2
#             l = self.get_item(nums, mid - 1)
#             r = self.get_item(nums, mid + 1)
#             target = self.get_item(nums, mid)
#             if target > l and target > r:
#                 return mid
#             elif target < r:
#                 start = mid + 1
#             else:
#                 end = mid - 1
