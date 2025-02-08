from typing import List
from string import ascii_lowercase
from collections import defaultdict


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        fs = [defaultdict(int) for _ in range(len(words))]
        for index, word in enumerate(words):
            for ch in word:
                fs[index][ch] += 1
        result = []
        for ch in words[0]:
            if all([f[ch] > 0 for f in fs]):
                for f in fs:
                    f[ch] -= 1
                result.append(ch)
        return result


print(
    Solution().commonChars(
        words=[
            "bbddabab",
            "cbcddbdd",
            "bbcadcab",
            "dabcacad",
            "cddcacbc",
            "ccbdbcba",
            "cbddaccc",
            "accdcdbb",
        ]
    )
)
