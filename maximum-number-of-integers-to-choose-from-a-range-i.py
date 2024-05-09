from typing import List


class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        s = set(banned)
        sm = 0
        count = 0
        i = 1
        while i < n+1:
            if i in s:
                pass
            else:
                if sm + i <= maxSum:
                    sm += i
                    count += 1
                else:
                    break
            i += 1
        return count


