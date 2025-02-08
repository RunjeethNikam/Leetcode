from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return [
            [num for index, num in enumerate(nums) if i & (1 << index)]
            for i in range(0, 1 << len(nums))
        ]


print(Solution().subsets(nums=[1, 2, 3]))
