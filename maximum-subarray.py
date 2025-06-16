from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def current(low, high, mid):
            sm = 0
            mx_left = float("-inf")
            for i in range(mid, low - 1, -1):
                sm += nums[i]
                mx_left = max(mx_left, sm)
            sm = 0
            mx_right = float("-inf")
            for i in range(mid + 1, high + 1):
                sm += nums[i]
                mx_right = max(mx_right, sm)
            return mx_left + mx_right

        def solve(low, high):
            if low == high:
                return nums[low]
            mid = (low + high) // 2
            left = solve(low, mid)
            right = solve(mid + 1, high)
            return max(left, right, current(low, high, mid))

        return solve(0, len(nums) - 1)


print(Solution().maxSubArray(nums = [5,4,-1,7,8]))
