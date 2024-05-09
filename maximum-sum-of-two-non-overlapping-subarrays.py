from typing import List

class Solution:

    def solve(self, nums, ln):
        dp = [0] * len(nums)
        sm = 0
        mx = float('-inf')
        for index, value in enumerate(nums):
            sm += value
            if index == (ln-1):
                mx = max(mx, sm)
                dp[index]= mx
            elif index > (ln - 1):
                sm -= nums[index-ln]
                mx = max(mx, sm)
                dp[index]= mx
        return dp

    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        dp1 = self.solve(nums, firstLen) # when firstLen is first
        dp2 = self.solve(nums, secondLen) # when secondLen is first
        dp3 = list(reversed(self.solve(list(reversed(nums)), firstLen))) # when f is second
        dp4 = list(reversed(self.solve(list(reversed(nums)), secondLen))) # when secondLen is second

        mx = float('-inf')
        for i in range(firstLen-1, len(nums) - secondLen):
            mx = max(mx, dp1[i] + dp4[i+1])
        for i in range(secondLen-1, len(nums) - firstLen):
            mx = max(mx, dp2[i] + dp3[i+1])
        
        return mx


            
print(Solution().maxSumTwoNoOverlap([1,2,3],1, 2))
            





        