from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        st = []
        for index, temp in enumerate(temperatures):
            if not st or temperatures[st[-1]] > temp:
                st.append(index)
            else:
                while st and temperatures[st[-1]] < temp:
                    result[st[-1]] = index - st[-1]
                    st.pop()
                st.append(index)
        return result
    

print(Solution().dailyTemperatures([73,74,75,71,69,72,76,73]))