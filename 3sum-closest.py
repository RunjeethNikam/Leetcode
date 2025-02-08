from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        result = float("inf")
        for left in range(len(nums) - 2):
            mid = left + 1
            right = len(nums) - 1
            while mid < right:
                sm = nums[left] + nums[mid] + nums[right]
                if sm == target:
                    return sm

                if abs(target - sm) < abs(result - target):
                    result = sm

                if sm < target:
                    mid += 1
                else:
                    right -= 1
        return result


print(Solution().threeSumClosest(nums=[-1, 2, 1, -4], target=1))
