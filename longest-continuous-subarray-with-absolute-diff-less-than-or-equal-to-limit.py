from typing import List
from heapq import *
from collections import deque


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        low = 0
        mx_q = deque([nums[0]])
        mn_q = deque([nums[0]])
        result = 0
        for high, value in enumerate(nums):
            heappush(mx_h, (-value, high))
            heappush(mn_h, (value, high))
            while mx_h and mx_h[0][1] < low:
                heappop(mx_h)
            while mn_h and mn_h[0][1] < low:
                heappop(mn_h)
            mx = -mx_h[0][0]
            mn = mn_h[0][0]
            if low <= high and (mx - mn) > limit:
                low += 1
                while mx_h and mx_h[0][1] < low:
                    heappop(mx_h)
                while mn_h and mn_h[0][1] < low:
                    heappop(mn_h)
                mx = -mx_h[0][0]
                mn = mn_h[0][0]
            result = max(result, high - low + 1)
        return result


print(Solution().longestSubarray(nums=[4, 2, 2, 2, 4, 4, 2, 2], limit=0))
