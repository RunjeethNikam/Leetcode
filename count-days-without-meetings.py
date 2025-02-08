from typing import List


class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        s, e = meetings[0]
        count = 0
        if s != 1:
            count += s - 1
        for start, end in meetings[1:]:
            if start > days:
                break
            if e < start:
                count += start - e - 1
                s = start
            e = max(e, end)

        if e <= days:
            count += days - e
        return count


print(Solution().countDays(days=8, meetings=[[2, 3], [3, 5], [8, 8]]))
