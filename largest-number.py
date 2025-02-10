from typing import List
from functools import cmp_to_key


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = list(map(lambda item: str(item), nums))

        def compare(a, b):
            if (a + b) > (b + a):
                return -1
            elif (b + a) > (a + b):
                return 1
            return 0

        nums.sort(key=cmp_to_key(compare))
        if nums[0] == '0':
            return '0'
        return "".join(nums)


print(Solution().largestNumber([3, 30, 34, 5, 9]))
