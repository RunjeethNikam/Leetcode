from collections import Counter

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        strs.sort(key=lambda given: ''.join(sorted(given)))
        result = []
        freq = None
        inner = []
        for item in strs:
            if len(inner) == 0:
                inner.append(item)
                freq = Counter(item)                    
            else:
                if Counter(item) == freq:
                    inner.append(item)
                else:
                    result.append(inner)
                    inner = [item]
                    freq = Counter(item)
        if inner:
            result.append(inner)
        return result
    
print(Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
print(Solution().groupAnagrams([""]))
print(Solution().groupAnagrams(["a"]))