from typing import List


class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        negative = None
        negatives_count = 0
        left = -1
        for index, value in enumerate(nums):
            if value == 0:
                negative = None
                negatives_count = 0
                left = index
            elif value > 0:
                dp[index] = 1 + (dp[index - 1] if index > 0 else 0)
            else:
                if (negatives_count % 2) == 1:
                    dp[index] = index - left
                else:
                    if not negative:
                        dp[index] = 0
                        negative = index
                    else:
                        dp[index] = index - negative
                negatives_count += 1
        return max(dp)


print(Solution().getMaxLen([0, 1, -2, -3, -4]))
