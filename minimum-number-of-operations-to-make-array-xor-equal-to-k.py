from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        xor = 0
        for num in nums:
           xor ^= num
        bin(xor ^ k).count('1')

print(Solution().minOperations(nums = [2,0,2,0], k = 0))
