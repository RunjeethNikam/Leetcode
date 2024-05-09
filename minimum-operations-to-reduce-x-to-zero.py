from typing import List


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        if x > sum(nums):
            return -1
        elif x == sum(nums):
            return len(nums)
        f = {}
        total_sum = 0
        for index, num in enumerate(nums):
            total_sum += num
            if total_sum not in f:
                f[total_sum] = index
        sm = 0
        result = float('inf')
        if x in f:
            result = f[x] + 1
        for index in range(len(nums)-1, -1, -1):
            del f[total_sum - sm]
            sm += nums[index]
            rm = x - sm
            if sm == x:
                result = min(result, len(nums) - index)
            elif rm in f:
                result = min(result, len(nums) - index  + f[rm] + 1)
            elif sm > x:
                break
        return result if result != float('inf') else -1
    
print(Solution().minOperations([5,2,3,1,1], 5))
            
