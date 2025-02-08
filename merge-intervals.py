class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort()
        s, e = intervals[0]
        result = []
        for start, end in intervals:
            if start > e:
                result.append([s, e])
                s = start
                e = end
            else:
                e = max(end)
        return result



Solution().merge([[2,6], [1,3],[8,10],[15,18]])