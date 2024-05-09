from typing import List


class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        result = float("-inf")
        i = values[0]
        for j in range(1, len(values)):
            result = max(result, i - (j - values[j]))
            i = max(i, values[j] + j)
        return result
