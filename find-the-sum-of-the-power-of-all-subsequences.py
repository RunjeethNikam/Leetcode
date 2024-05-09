from typing import List



class Solution:
    def sumOfPower(self, nums: List[int], k: int) -> int:
        def solve(i, sm):
            if sm == 0:
                return 1
            if i >= 0:
                result = 0
                for left in range(i-1, -1, -1):
                    result += solve(left, sm - nums[i])
                result += solve(i - 1, sm)
                return result
            return 0

            
        
        # result = 0
        return solve(len(nums)-1, k)
        # for i in range(len(nums)):
        #     result += solve(len(nums)-1, k)
    

print(Solution().sumOfPower([1,2,3], 3))