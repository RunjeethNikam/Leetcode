from typing import List


class Solution:

    def largestRectangleArea(self, heights: List[int]) -> int:
        st = []
        result = float("-inf")
        for index, h in enumerate(heights):
            while st and heights[st[-1]] > h:
                top = st.pop()
                value = heights[top]
                if st:
                    result = max(result, value * (index - st[-1] - 1))
                else:
                    result = max(result, value * index)
            st.append(index)

        if st:
            left = -1
            right = st[-1]
            for index in st:
                result = max(result, heights[index] * (right - left))
                left = index

        return result

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        h = [0] * len(matrix[0])
        result = float("-inf")

        for r in matrix:
            for index, height in enumerate(r):
                if height == '0':
                    h[index] = 0
                else:
                    h[index] += 1
            result = max(result, self.largestRectangleArea(h))

        return result


print(
    Solution().maximalRectangle(
        [
            ["1", "0", "1", "0", "0"],
            ["1", "0", "1", "1", "1"],
            ["1", "1", "1", "1", "1"],
            ["1", "0", "0", "1", "0"],
        ]
    )
)
