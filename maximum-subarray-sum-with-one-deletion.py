from typing import List


class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        left = [0] * len(arr)
        right = [0] * len(arr)
        for index, value in enumerate(arr):
            if index > 0:
                left[index] = max(left[index - 1] + arr[index - 1], arr[index - 1])
        for index in range(len(arr) - 2, -1, -1):
            if index < len(arr) - 1:
                right[index] = max(right[index + 1] + arr[index + 1], arr[index + 1])


        # return max(*[l + r for l, r in zip(left, right)], *left, *right)


print(Solution().maximumSum([-1,-1,-1,-1]))
