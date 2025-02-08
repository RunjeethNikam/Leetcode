from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        candidate1 = nums[0]
        result = []
        count = 1
        for num in nums[1:]:
            if num != candidate1:
                count -= 1
            else:
                count += 1
            if count == 0:
                candidate1 = num
        count = 0
        for num in nums:
            count += num == candidate1
        if count > len(nums)/3:
            result.append(candidate1)
        count = 0
        candidate = None
        for num in nums:
            if num != candidate1:
                

    