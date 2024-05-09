from typing import List


class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        s = []
        i = 0
        while i < len(nums) and (len(s) + len(nums) - i) > k:
            if len(s) == 0 or s[-1] <= nums[i]:
                s.append(nums[i])
                i += 1
            elif s[-1] > nums[i]:
                s.pop()
        if (len(s) + len(nums) - i) == k:
            return s + nums[i:]
        return  s[:k]
        

print(Solution().mostCompetitive([6,4,3,3,5,4,9,2], 4))

            