from typing import List


class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        s = []
        count = 0
        for num in nums:
            c = 0
            while s and num < s[-1]:
                c += 1
                s.pop()
            count = max(count, c)
            s.append(num)
        return count


print(Solution().totalSteps([10, 1, 2, 3, 4, 5, 6, 1, 2, 3]))
