from typing import List


class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        sm = neededTime[0]
        mn = neededTime[0]
        result = 0

        for index, color in enumerate(colors):
            if index > 0:
                if colors[index - 1] != color:
                    result += sm - mn
                    sm = neededTime[index]
                    mn = neededTime[index]
                else:
                    sm += neededTime[index]
                    mn = max(mn, neededTime[index])
        result += sm - mn

        return result


print(Solution().minCost("aabaa", [1,2,3,4,1]))
