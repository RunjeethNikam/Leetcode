from typing import List


class Solution:

    # def add(self, t, word):
    #     pass

    

    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        count = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                a, b = words[i], words[j]
                if b.startswith(a) and b.endswith(a):
                    count += 1
        # self.prefix_trie = {}
        # self.suffix_trie = {}
        # words.sort(key= lambda _: len(_))

        # for word in words:
        #     self.add(self.prefix_trie, word)
        #     self.add(self.suffix_trie, word[::-1])

        
