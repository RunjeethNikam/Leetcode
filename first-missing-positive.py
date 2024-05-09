from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            if nums[i] < 0:
                nums[i] = 0
            i += 1

        for index, value in enumerate(nums):
            if value == 0:
                continue
            v = abs(value)
            if v < (len(nums)+1):
                if nums[v-1] == 0:
                    nums[v-1] = -v
                else:
                    nums[v-1] = -(abs(nums[v-1]))
            
        

        i = 0
        while i < len(nums):
            if nums[i] >= 0:
                return i+1
            i += 1
        return i+1
    
print(Solution().firstMissingPositive([7,8,9,11,12]))