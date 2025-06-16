from typing import List
from collections import defaultdict


class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        subset_sums = [{0} for _ in range(len(nums))]
        for k, (l, r, v) in enumerate(queries):
            print(subset_sums)
            if all(x in st for x, st in zip(nums, subset_sums)):
                return k
            for i in range(l, r + 1):
                sums = []
                for x in subset_sums[i]:
                    sums.append(x + v)
                subset_sums[i].update(sums)
        # return len(queries) if all(x in st for x, st in zip(nums, subset_sums)) else -1


# print(
#     Solution().minZeroArray(
#         nums=[1, 2, 3, 2, 1],
#         queries=[[0, 1, 1], [1, 2, 1], [2, 3, 2], [3, 4, 1], [4, 4, 1]],
#     )
# )
# print(Solution().minZeroArray(nums=[4, 3, 2, 1], queries=[[1, 3, 2], [0, 2, 1]]))
print(
    Solution().minZeroArray(nums=[2, 0, 2], queries=[[0, 2, 1], [0, 2, 1], [1, 1, 3]])
)
