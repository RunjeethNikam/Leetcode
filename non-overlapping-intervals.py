from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # intervals.sort(key= lambda _: (_[0], _[1]))
        intervals.sort()
        start = float('-inf')
        end = float('-inf')
        count = 0
        for interval in intervals:
            if interval[0] >= end:
                start = interval[0]
                end = interval[1]
            elif interval[0] >= start and interval[1] <= end:
                start = interval[0]
                end = interval[1]
            else:
                count += 1
        return count

        # print(intervals)


print(Solution().eraseOverlapIntervals([[-52,31],[-73,-26],[82,97],[-65,-11],[-62,-49],[95,99],[58,95],[-31,49],[66,98],[-63,2],[30,47],[-40,-26]]))
