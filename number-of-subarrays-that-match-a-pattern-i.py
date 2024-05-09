from typing import List


class Solution:
    def check(self, temp, pattern, start):
        i = 0
        while i < len(pattern) and start < len(temp):
            if temp[start] == pattern[i]:
                start += 1
                i += 1
            else:
                return False
        if i == len(pattern):
            return True
        else:
            return False



    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        temp = []
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                temp.append(0)
            elif nums[i] > nums[i-1]:
                temp.append(1)
            else:
                temp.append(-1)
        count = 0
        for i in range(len(temp)):
            if temp[i] == pattern[0] and self.check(temp, pattern, i):
                count += 1
        return count
    
print(Solution().countMatchingSubarrays([1,1], [-1]))