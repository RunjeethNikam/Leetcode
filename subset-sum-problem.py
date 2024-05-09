from typing import List


class Solution:
    # def isSubsetSum (self, arr, sum):
    #     dp = [False] * (sum+1)
    #     for num in arr:
    #         temp = dp[:]
    #         for j in range(num, sum+1):
    #             temp[j] = dp[j] or dp[j-num]
    #         if num < len(dp):
    #             temp[num] = True
    #         for i in range(len(temp)):
    #             dp[i] = dp[i] or temp[i]
    #     return dp[-1]

    def canPartition(self, nums: List[int]) -> bool:
        sm = sum(nums)
        if (sm % 2) == 0:
            possible_sums = set()
            possible_sums.add(0)
            for num in nums:
                possible_sums.update(
                    [existing_sum + num for existing_sum in possible_sums]
                )
                if (sm//2) in possible_sums:
                    return True
        return False


print(Solution().canPartition([1,5,11,5]))
