import math
from collections import defaultdict


class Solution:
    def minimumPushes(self, word: str) -> int:
        freq_map = defaultdict(int)
        for ch in word:
            freq_map[ch] += 1

        freq_map_sorted = list(
            map(lambda x: x[0], sorted(freq_map.items(), key=lambda x: x[1]))
        )[::-1]
        count = 8
        f = {}
        result = 0
        for key in freq_map_sorted:
            f[key] = math.floor(count / 8)
            count += 1
        for ch in word:
            result += f[ch]
        return result
    
print(Solution().minimumPushes("abcde"))
