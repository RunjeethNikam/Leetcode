class Solution:
    def matrixMultiplication(self, arr):
        dp = [[float("inf")] * len(arr) for _ in range(len(arr))]
        for i in range(len(arr)):
            dp[i][i] = 0

        for size in range(2, len(arr)):
            for left in range(len(arr) - size):
                right = left + size
                for p in range(left + 1, left + size):
                    value = (
                        dp[left][p]
                        + dp[p + 1][right]
                        + arr[left] * arr[p + 1] * arr[right]
                    )
                    dp[left][right] = min(dp[left][right], value)
        return dp[0][-1]


print(Solution().matrixMultiplication([40, 20, 30, 10, 30]))


# {40, 20, 30, 10, 30}
