from typing import List
from collections import deque


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        mx = max(nums)
        q = deque()
        result = 0
        for index, num in enumerate(nums):
            if num == mx:
                q.append(index)
            if len(q) > k:
                q.popleft()
            if len(q) == k:
                result += (q[0] + 1)
        return result


print(Solution().countSubarrays([1,1], 1))