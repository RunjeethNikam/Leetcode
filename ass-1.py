from typing import List
from collections import Counter


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        d = Counter(arr1)
        result = []
        for item in arr2:
            result.extend([item] * d[item])
            del d[item]
        r = []
        for key in d.keys():
            r.extend([key] * d[key])
        r.sort()
        result.extend(r)
        return result

# You have n dice, and each dice has k faces numbered from 1 to k.


print(
    Solution().relativeSortArray([2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19], [2, 1, 4, 3, 9, 6])
)
