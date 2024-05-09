from collections import defaultdict
from typing import List


class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        d = defaultdict(int)
        mx = float('-inf')
        number_of_elements = 0
        for num in nums:
            d[num] += 1
            if d[num] > mx:
                number_of_elements = 1
                mx = d[num]
            elif d[num] == mx:
                number_of_elements += 1
        return number_of_elements * mx
    
print(Solution().maxFrequencyElements([1,2,2,3,1,4]))