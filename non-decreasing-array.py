from typing import List


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        nums.append(float("inf"))
        nums.insert(0, float("-inf"))
        left = [0]
        for i in range(1, len(nums)):
            left.append(left[-1] + (1 - int(nums[i - 1] <= nums[i])))
        right = [0]
        for i in range(len(nums) - 2, -1, -1):
            right.append(right[-1] + (1 - int(nums[i] <= nums[i + 1])))
        right.reverse()
        for i in range(1, len(nums) - 1):
            l = 0
            if i != 0:
                l = left[i - 1]
            r = 0
            if i != len(nums) - 1:
                r = right[i + 1]
            if l == 0 and r == 0 and nums[i - 1] <= nums[i + 1]:
                return True

        return False


print(Solution().checkPossibility(nums=[4, 2, 3]))
