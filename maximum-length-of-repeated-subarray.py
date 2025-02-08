from typing import List


class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        l1 = len(nums1)
        l2 = len(nums2)
        dp = [[0] * (l2 + 1) for _ in range((l1 + 1))]
        for i in range(1, l1 + 1):
            for j in range(1, l2 + 1):
                if nums1[i - 1] == nums2[j - 1]:
                    last1 = -1
                    last2 = -1
                    if i > 1:
                        last1 = nums1[i - 2]
                    if j > 1:
                        last2 = nums2[j - 2]
                    if last1 == last2:
                        dp[i][j] = 1 + dp[i - 1][j - 1]
                    else:
                        dp[i][j] = 1
                else:
                    dp[i][j] = 0
        result = 0
        for i in dp:
            for j in i:
                if j > result:
                    result = j
        return result


print(Solution().findLength(nums1 = [0,0,0,0,0], nums2 = [0,0,0,0,0]))
