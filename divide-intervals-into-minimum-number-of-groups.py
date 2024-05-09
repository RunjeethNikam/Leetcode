from typing import List
from heapq import *


class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        running = []
        intervals.sort()
        count = 0
        for start, end in intervals:
            if running and start > running[0]:
                heappushpop(running, end)
            else:
                heappush(running, end)
            count = max(count, len(running))
        return count


print(Solution().minGroups([[5,10],[6,8],[1,5],[2,3],[1,10]]))
