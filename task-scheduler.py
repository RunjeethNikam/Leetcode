from typing import List
from collections import Counter
from string import ascii_uppercase
import heapq


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        c = Counter(tasks)

        h = []
        for value in c.values():
            heapq.heappush(h, -value)

        count = 0
        n += 1
        while len(h):
            used_ch = 0
            a = []
            while used_ch < n and len(h):
                used_ch += 1
                f = -heapq.heappop(h)
                if f > 1:
                    a.append(f-1)
            for f in a:
                heapq.heappush(h, -f)
            if len(h) == 0:
                count += used_ch
            else:
                count += max(used_ch, n)
        return count


print(
    Solution().leastInterval(
        ["A", "A", "A", "B", "B", "B", "C", "C", "C", "D", "D", "E"], 2
    )
)
