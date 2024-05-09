from typing import List
from collections import deque, defaultdict


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        mp = defaultdict(list)
        lnth = len(beginWord)
        for word in wordList:
            for i in range(lnth):
                wd = word[:i] + "*" + word[i + 1 :]
                mp[wd].append(word)

        q = deque([[beginWord, 1]])
        seen = set()
        while len(q):
            wd, step = q.popleft()
            for i in range(lnth):
                wildcard = wd[:i] + "*" + wd[i + 1 :]
                for mutation in mp[wildcard]:
                    if mutation not in seen:
                        if mutation == endWord:
                            return step + 1
                        else:
                            q.append([mutation, step + 1])
                        seen.add(mutation)
        return 0


print(Solution().ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
