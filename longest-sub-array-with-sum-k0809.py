class Solution:
    def lenOfLongSubarr(self, arr, n, k):

        d = {}
        count = 0
        result = 0
        for index, num in enumerate(arr):
            count += num
            if count not in d:
                d[count] = index
            if count == k:
                result = max(result, index + 1)
            if (count - k) in d:
                result = max(result, index - d[count - k])
        return result


print(
    Solution().lenOfLongSubarr(
        [-13, 0, 6, 15, 16, 2, 15, -12, 17, -16, 0, -3, 19, -3, 2, -9, -6], 17, 15
    )
)

