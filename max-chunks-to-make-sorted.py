from typing import List


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        count = 0
        mx = -1
        for index in range(len(arr)):
            mx = max(mx, arr[index])
            if mx == index:
                count += 1
        return count
