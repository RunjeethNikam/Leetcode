from typing import List
from collections import Counter

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        f = Counter(arr)
        for num in arr:
            if num != 0 and num*2 in f:
                return True
            if num == 0 and f[0] > 1:
                return True
        return False

print(Solution().checkIfExist([-2,0,10,-19,4,6,-8]))
