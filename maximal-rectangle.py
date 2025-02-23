from typing import List


class Solution:

    # def largestRectangleArea(self, heights: List[int]) -> int:
    #     st = []
    #     result = float("-inf")
    #     for index, h in enumerate(heights):
    #         while st and heights[st[-1]] > h:
    #             top = st.pop()
    #             value = heights[top]
    #             if st:
    #                 result = max(result, value * (index - st[-1] - 1))
    #             else:
    #                 result = max(result, value * index)
    #         st.append(index)

    #     if st:
    #         left = -1
    #         right = st[-1]
    #         for index in st:
    #             result = max(result, heights[index] * (right - left))
    #             left = index

    #     return result

    # def maximalRectangle(self, matrix: List[List[str]]) -> int:
    #     h = [0] * len(matrix[0])
    #     result = float("-inf")

    #     for r in matrix:
    #         for index, height in enumerate(r):
    #             if height == '0':
    #                 h[index] = 0
    #             else:
    #                 h[index] += 1
    #         result = max(result, self.largestRectangleArea(h))

    #     return result

    def solve(self, given):
        st = [(-1, float("-inf"))]
        r = float("-inf")
        for index, value in enumerate(given):
            while st[-1][1] > value:
                _, height = st.pop()
                r = max(r, height * (index - st[-1][0] - 1))

            st.append((index, value))
        while st:
            _, height = st.pop()
            r = max(r, height * (len(given) - st[-1][0] - 1))
        return r

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        matrix = [list(map(int, m)) for m in matrix]
        result = [0] * len(matrix[0])
        r = 0
        for m in matrix:
            result = [a + b for a, b in zip(result, m)]
            r = max(r, self.solve(result))
        return r


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
