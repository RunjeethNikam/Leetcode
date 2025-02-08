from typing import List
from collections import Counter


class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        c = Counter(nums)
        count = len(c.keys())
        result = []
        while count > 0:
            temp = []
            for k in list(c.keys()):
                if c[k] > 0:
                    temp.append(k)
                    c[k] -= 1
                elif c[k] == 0:
                    del c[k]
                    count -= 1
            if temp:
                result.append(temp)
        return result


print(Solution().findMatrix(nums=[1, 3, 4, 1, 2, 3, 1]))
