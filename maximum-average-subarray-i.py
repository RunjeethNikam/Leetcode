from typing import List



class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        w = sum(nums[:k])
        mx = w
        for i in range(len(nums) - k):
            w = w - nums[i] + nums[i+k]
            mx = max(mx, w)
        return mx / k
    
print(Solution().findMaxAverage([1,12,-5,-6,50,3], 4))