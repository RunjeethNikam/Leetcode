from typing import List
from functools import cmp_to_key


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # Convert each integer to a string
        num_strings = [str(num) for num in nums]

        def compare(a, b):
            if (a + b) < (b + a):
                return -1  # a will come first
            elif (a + b) > (b + a):
                return 1  # b will come first
            return 0

        num_strings.sort(key=cmp_to_key(compare), reverse=True)

        if num_strings[0] == "0":
            return "0"

        return "".join(num_strings)


Solution().largestNumber([3, 30, 34, 5, 9])
