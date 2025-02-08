from collections import deque
from typing import List


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        q = deque()
        last = 0
        result = 0
        for index, value in enumerate(nums):
            if value % 2 == 1:
                q.append(index)
            while len(q) > k:
                p = q.popleft()
                last = p + 1
            if len(q) == k:
                result += q[0] - last + 1
        return result


print(Solution().numberOfSubarrays([2, 2, 2, 1, 2, 2, 1, 2, 2, 2], 2))
