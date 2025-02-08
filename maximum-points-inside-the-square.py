from typing import List
from collections import defaultdict


class Solution:
    def maxPointsInsideSquare(self, points: List[List[int]], s: str) -> int:

        dp = defaultdict(list)
        for tag, (x, y) in zip(s, points):
            dp[max(abs(x), abs(y))].append(tag)

        count = 0
        seen_tags = set()
        dp = sorted(dp.items())
        for _, tags in dp:
            if len(set(tags)) != len(tags) or any([tag in seen_tags for tag in tags]):
                break
            else:
                count += len(tags)
                seen_tags.update(tags)
        return count


print(
    Solution().maxPointsInsideSquare(
        points=[[2, 2], [-1, -2], [-4, 4], [-3, 1], [3, -3]], s="abdca"
    )
)
