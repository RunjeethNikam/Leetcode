from collections import Counter



class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        c1 = Counter(word1)
        c2 = Counter(word2)

        s1 = sorted(c1.values())
        s2 = sorted(c2.values())

        if len(s1) != len(s2):
            return False
        for v1, v2 in zip(s1, s2):
            if v1 != v2:
                return False
            
        return True
