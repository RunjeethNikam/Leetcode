from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        mx = float('-inf')
        curr = 1
        for num in nums:
            curr *= num
            mx = max(curr, mx)
            if curr == 0:
                curr = 1

        curr = 1
        for num in nums[::-1]:
            curr *= num
            mx = max(curr, mx)
            if curr == 0:
                curr = 1

        return mx
    

print(Solution().maxProduct([2,3,-2, -1,4]))

        