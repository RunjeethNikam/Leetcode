from typing import *


class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        if len(nums) == 1:
            result = []
            for s, e in queries:
                result.append(True)
            return result
        prefix_arr = []
        for i in range(1, len(nums)):
            prefix_arr.append(int(nums[i] % 2 == nums[i - 1] % 2))
        count = prefix_arr[0]
        for i in range(1, len(prefix_arr)):
            count += prefix_arr[i]
            prefix_arr[i] = count

        result = []
        for start, end in queries:
            if start == end:
                result.append(True)
            elif start == 0:
                if prefix_arr[end - 1] > 0:
                    result.append(False)
                else:
                    result.append(True)
            else:
                if (prefix_arr[end - 1] - prefix_arr[start - 1]) > 0:
                    result.append(False)
                else:
                    result.append(True)
        return result


print(Solution().isArraySpecial(nums=[3,1], queries=[[0, 0]]))
