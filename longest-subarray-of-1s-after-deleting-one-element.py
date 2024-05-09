from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        i = 0
        count = 0
        mx = -1
        for index, num in enumerate(nums):
            if num == 1:
                pass
            else:
                count += 1
                while count > 1:
                    if nums[i] == 0:
                        count -= 1
                    i += 1
            mx = max(index - i, mx)
        return mx


print(Solution().longestSubarray([1,1,1,1,1]))
