from collections import Counter
from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        visited = set()
        c = Counter(s)
        left = 0
        result = []
        for index, ch in enumerate(s):
            if ch not in visited:
                visited.add(ch)
            c[ch] -= 1
            if c[ch] == 0:
                visited.remove(ch)
            if len(visited) == 0:
                result.append(index - left + 1)
                left = index + 1
        return result


print(Solution().partitionLabels("ababcbacadefegdehijhklij"))
