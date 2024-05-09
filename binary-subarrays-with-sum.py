from typing import List


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        if goal > sum(nums):
            return -1

        def solve(i, j):
            if goal == 0:
                count = j - i + 1
                return count * (count + 1) // 2
            else:
                left = right = 0
                while i < len(nums) and nums[i] == 0:
                    left += 1
                    i += 1
                
                while j >= 0 and nums[j] == 0:
                    right += 1
                    j -= 1
                
                return (left * right) + left + right + 1


        i = 0
        j = 0
        count = 0
        result = 0
        while j < len(nums):
            if nums[j] == 1:
                count += 1
                if count > goal:
                    result += solve(i, j-1)
                    while count > goal:
                        if nums[i] == 1:
                            count -= 1
                        i += 1
                else:
                    pass
            else:
                pass
            j += 1
        
        while count > goal:
            if nums[i] == 1:
                count -= 1
            i += 1
        
        result += solve(i, j-1)
        
        return result
    

print(Solution().numSubarraysWithSum([0,0, 0,0,0], 0))
        

        
        

        
        
            
            