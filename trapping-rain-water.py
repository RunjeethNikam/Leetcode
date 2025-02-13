from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        st = []
        result = 0
        for r, rh in enumerate(height):
            level = 0
            while st and st[-1][1] <= rh:
                l, lh = st[-1]
                dist = r - l - 1
                result += dist * (min(rh, lh) - level)
                level = max(level, lh)
                st.pop()
            if st:
                l, lh = st[-1]
                dist = r - l - 1
                result += dist * (min(rh, lh) - level)
            st.append((r, rh))
        return result


print(Solution().trap(height = [4,2,0,3,2,5]))
