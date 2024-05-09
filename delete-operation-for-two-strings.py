from collections import Counter



class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        w1 = Counter(word1)
        w2 = Counter(word2)
        result = 0

        for ch, value in w1.items():
            if ch in w2:
                result += max(value - w2[ch], 0)
            else:
                result += value
        
        for ch, value in w2.items():
            if ch in w1:
                result += max(value - w1[ch], 0)
            else:
                result += value
        
        return result

print(Solution().minDistance('leetcode', 'etco'))