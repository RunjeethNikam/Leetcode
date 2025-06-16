from typing import List


class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:


        def solve(time):
            pass

        low = 0
        high = 0
        ans = None
        for s in skill:
            for m in mana:
                high += s * m
        
        while low <= high:
            mid = (low + high) // 2
            if solve(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

