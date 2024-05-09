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
                left = result

        return result


print(Solution().largestRectangleArea([1, 2,  2]))
