from typing import List


class Solution:

    def canBeIncreasing(self, nums: List[int]) -> bool:
        lt1 = float('-inf')
        lt2 = float('-inf')
        count = 0
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                count += 1
            if nums[i] < nums[i-1]:
                if nums[i] < nums[i-2]:
                    count += 1
            if count >= 2:
                return False
        return True

        


    
print(Solution().canBeIncreasing([1,2,10,5,7]))
# print(Solution().canBeIncreasing([2,3,1,2]))
# print(Solution().canBeIncreasing([1,1,1]))
# print(Solution().canBeIncreasing([105,924,32,968]))

