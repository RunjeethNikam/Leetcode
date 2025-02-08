from collections import defaultdict
from typing import List

from functools import cache


class Solution:

    def create_trie(self, words, costs):
        t = {}
        for word, cost in zip(words, costs):
            temp = t
            for ch in word:
                if ch not in temp:
                    temp[ch] = {}
                temp = temp[ch]
            if "*" in temp:
                temp["*"] = min(cost, temp["*"])
            else:
                temp["*"] = cost
        return t

    def minimumCost(self, target: str, words: List[str], costs: List[int]) -> int:
        trie = self.create_trie(words, costs)
        n = len(target)
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        for i in range(n):
            if dp[i] == float('inf'):
                continue
            node = trie
            for j in range(i, n):
                if target[j] not in node:
                    break
                node = node[target[j]]
                if '*' in node:
                    dp[j + 1] = min(dp[j + 1], dp[i] + node['*'])
        return dp[n] if dp[n] != float('inf') else -1



print(Solution().minimumCost(target = "abcdef", words = ["abdef","abc","d","def","ef"], costs = [100,1,1,10,5]))
