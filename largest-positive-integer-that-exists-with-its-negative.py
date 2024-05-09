from typing import List


class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        hash_map = set()
        ans = -1

        for num in nums:
            if -num in hash_map and ans < abs(num):
                ans = abs(num)
            hash_map.add(num)

        return ans


print(Solution().findMaxK([-10, 8, 6, 7, -2, -3]))
