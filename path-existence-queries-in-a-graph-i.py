from typing import List


class Solution:
    def pathExistenceQueries(
        self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]
    ) -> List[bool]:
        prefix = [0]
        count = 0
        for i in range(1, len(nums)):
            count += bool(abs(nums[i-1] - nums[i]) <= maxDiff)
            prefix.append(count)

        result = []
        for u, v in queries:
            result.append(prefix[u] == prefix[v])
        return result


print(
    Solution().pathExistenceQueries(
        n=4, nums=[2, 5, 6, 8], maxDiff=2, queries=[[0, 1], [0, 2], [1, 3], [2, 3]]
    )
)
