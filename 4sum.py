from typing import List
from collections import defaultdict


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = list(set(nums))
        nums.sort()
        result = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                k, l = j + 1, len(nums) - 1
                while k < l:
                    sm = nums[i] + nums[j] + nums[k] + nums[l]
                    if sm == target:
                        result.append([nums[i], nums[j], nums[k], nums[l]])
                    elif sm < target:
                        k += 1
                    else:
                        l -= 1
        return result


print(Solution().fourSum(nums=[1, 0, -1, 0, -2, 2], target=0))
