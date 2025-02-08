from collections import defaultdict
from typing import List


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        record = defaultdict(lambda: defaultdict(int))
        for w, l in matches:
            record[w][1] += 1
            record[l][0] += 1
        result = [[], []]
        for p, stats in record.items():
            if stats[0] == 0:
                result[0].append(p)
            if stats[0] == 1:
                result[1].append(p)
        result[0].sort()
        result[1].sort()
        return result



print(
    Solution().findWinners(
        [
            [1, 3],
            [2, 3],
            [3, 6],
            [5, 6],
            [5, 7],
            [4, 5],
            [4, 8],
            [4, 9],
            [10, 4],
            [10, 9],
        ]
    )
)
