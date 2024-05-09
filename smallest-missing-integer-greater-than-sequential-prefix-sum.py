from typing import List
from collections import Counter


class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        freq = Counter(nums)
        lt = nums[0]
        sm = lt
        for i in range(1, len(nums)):
            if nums[i] - lt == 1:
                lt = nums[i]
                sm += nums[i]
            else:
                break
        start = sm 
        increment = 0
        if start not in freq:
            return start
        while True:
            if (start  + 2 ** increment) in freq:
                increment += 1
            elif increment != 0:
                start = start + 2 ** (increment-1)
                increment = 0
            else:
                start = start  + 2 ** increment
                break
        return start

print(Solution().missingInteger([2,24,49,27,45,44,45,39,14,2,43,10,30,6,23,40,48,48,43,14,37,8,15,21,23,9,15,30,48,46,12,4,31,38,47,48,43,47,40,43,8,25,8,17,40,3,41,32,22,16]))