from typing import List


# Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda item: item.end)
        st = []
        for interval in intervals:
            while st and st[0].end >= interval.start:
                interval.start = min(st[0].start, interval.start)
                st.pop()
            st.append(interval)
        return len(st)


interval_tuples = [(0, 40), (5, 10), (15, 20)]
intervals = [Interval(start, end) for start, end in interval_tuples]

print(Solution().minMeetingRooms(intervals))