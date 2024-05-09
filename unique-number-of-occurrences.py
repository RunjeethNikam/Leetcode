from typing import List
from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        c = Counter(arr)
        s = set()
        for value in c.values():
            if value in s:
                return False
            else:
                s.add(value)
        return True
