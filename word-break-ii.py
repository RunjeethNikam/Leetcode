from typing import List
from collections import defaultdict


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        trie = dict()
        for word in wordDict:
            t = trie
            for ch in word:
                if ch not in t:
                    t[ch] = {}
                t = t[ch]
            t["*"] = defaultdict()
        result = []

        def solve(i: int, path: list, current_trie: dict):
            if i == len(s) and '*' in current_trie:
                result.append(''.join(path))
                return 
            if i == len(s) or ('*' not in current_trie and s[i] not in current_trie):
                return

            if '*' not in current_trie:
                path.append(s[i])
                solve(i + 1, path, current_trie[s[i]])
                path.pop()
            if '*' in current_trie:
                path.append(' ')
                solve(i, path, trie)
                path.pop()

                if s[i] in current_trie:
                    path.append(s[i])
                    solve(i + 1, path, current_trie[s[i]])
                    path.pop()

        solve(0, [], trie)
        return result


print(
    Solution().wordBreak(s="pineapplepenapple", wordDict=["apple","pen","applepen","pine","pineapple"])
)
