from typing import List


class Solution:

    def get_index(self, nums, i):
        if i < 0:
            return 0
        return nums[i]

    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        dp = [0] * len(arr)
        i = 0
        # for i in range(len(arr)):
        while i < len(arr):
            mx = float('-inf')
            count = 1
            j = i
            # for j in range(i, max(-1, i-k), -1):
            while j > max(-1, i-k):
                mx = max(mx, self.get_index(arr, j))
                dp[i] = max(dp[i], self.get_index(dp, j-1) + count * mx)
                count += 1
                j -= 1
            i += 1
        return dp[-1]

print(Solution().maxSumAfterPartitioning([9,15,1,2], 3))