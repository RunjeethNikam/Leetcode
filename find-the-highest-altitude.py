from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        mx = 0
        curr = 0
        for g in gain:
            curr += g
            mx = max(mx, curr)
        return mx