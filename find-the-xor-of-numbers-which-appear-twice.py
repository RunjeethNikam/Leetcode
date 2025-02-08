from collections import Counter
from typing import List


class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        xor = 0
        c = Counter(nums)
        for key, value in c.items():
            if value == 2:
                xor ^= key
        return key
        

print(Solution().duplicateNumbersXOR([1,2,1,3]))