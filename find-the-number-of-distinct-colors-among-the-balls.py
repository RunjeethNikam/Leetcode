from typing import List
from collections import defaultdict


class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        # index_to_color_mapping = [0] * (limit+1)
        index_to_color_mapping = defaultdict(int)
        color_freq = defaultdict(int)
        result = []
        for index, color in queries:
            existing_color = index_to_color_mapping[index]
            index_to_color_mapping[index] = color
            if existing_color != color and existing_color != 0:
                if color_freq[existing_color] == 1:
                    del color_freq[existing_color]
                else:
                    color_freq[existing_color] -= 1
            if existing_color != color:
                color_freq[color] += 1
            result.append(len(color_freq.keys()))
        return result


print(Solution().queryResults(limit=1, queries=[[0,1],[0,4],[0,4],[0,1],[1,2]]))
