from typing import List



class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        s = []
        for num in nums:
            if not s or num < s[-1][0]:
                s.append((num, 0))
            else:
                c = 0
                while s and num > s[-1][0]:
                    top = s.pop()
                    c = max(c, top[1])
                s.append((num, c + 1))
        print(s)


print(Solution().totalSteps([4,5,7,7,13]))
                

