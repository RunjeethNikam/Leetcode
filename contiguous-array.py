from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        d = {}
        count = 0
        result = 0
        for index, num in enumerate(nums):
            if num:
                count += 1
            else:
                count -= 1

            if count == 0:
                result = max(result, index + 1)
            else:
                if count not in d:
                    d[count] = index
                else:
                    result = max(result, index - d[count])
        return result


print(
    Solution().findMaxLength(
        [
            0,
            1,
            0,
            1,
            1,
            1,
            0,
            0,
            1,
            1,
            0,
            1,
            1,
            1,
            1,
            1,
            1,
            0,
            1,
            1,
            0,
            1,
            1,
            0,
            0,
            0,
            1,
            0,
            1,
            0,
            0,
            1,
            0,
            1,
            1,
            1,
            1,
            1,
            1,
            0,
            0,
            0,
            0,
            1,
            0,
            0,
            0,
            1,
            1,
            1,
            0,
            1,
            0,
            0,
            1,
            1,
            1,
            1,
            1,
            0,
            0,
            1,
            1,
            1,
            1,
            0,
            0,
            1,
            0,
            1,
            1,
            0,
            0,
            0,
            0,
            0,
            0,
            1,
            0,
            1,
            0,
            1,
            1,
            0,
            0,
            1,
            1,
            0,
            1,
            1,
            1,
            1,
            0,
            1,
            1,
            0,
            0,
            0,
            1,
            1,
        ]
    )
)
