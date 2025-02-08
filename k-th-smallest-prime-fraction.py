from typing import List
from heapq import *


class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        h = [[arr[0] / arr[-1], 0, len(arr) - 1]]
        s = set()
        while k > 1:
            _, i, j = heappop(h)
            if (i + 1) < j and (i + 1, j) not in s:
                heappush(h, [arr[i + 1] / arr[j], i + 1, j])
                s.add((i + 1, j))
            if i < (j - 1) and (i, j - 1) not in s:
                heappush(h, [arr[i] / arr[j - 1], i, j - 1])
                s.add((i, j - 1))
            k -= 1
        _, i, j = heappop(h)
        return [arr[i], arr[j]]

    # def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
    #     s = []
    #     for i in range(len(arr)):
    #         for j in range(i):
    #             s.append(
    #                 (arr[j] / arr[i], j, i)
    #             )
    #     s.sort()
    #     print(s[:k+2])


print(Solution().kthSmallestPrimeFraction([1, 7, 23, 29, 47], 8))
