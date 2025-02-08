from typing import List
from collections import defaultdict


class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        count = defaultdict(int)
        index_sum = defaultdict(int)
        count[0] = 1
        result = 0
        running_xor = 0
        for index, num in enumerate(arr):
            running_xor ^= num
            if running_xor in count:
                result += index * count[running_xor] - index_sum[running_xor]
            count[running_xor] += 1
            index_sum[running_xor] += index + 1
        return result


print(Solution().countTriplets(arr = [2,3,1,6,7]))
