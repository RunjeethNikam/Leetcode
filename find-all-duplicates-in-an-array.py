from typing import List



class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = []
        for value in nums:
            num = abs(value)
            if nums[num-1] < 0:
                result.append(num)
            else:
                nums[num-1] = -nums[num-1]
        for i in range(len(nums)):
            nums[i] = abs(nums[i])

        return result
    

print(Solution().findDuplicates([4,3,2,7,8,2,3,1]))
