from typing import List


class Solution:

    def create_trie(self, dictionary: List[str]):
        t = {}
        for word in dictionary:
            temp = t
            for ch in word:
                if ch not in temp:
                    temp[ch] = {}
                temp = temp[ch]
            temp["*"] = "*"
        return t

    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        t = self.create_trie(dictionary)
        sentence = sentence.split()
        for i in range(len(sentence)):
            word = sentence[i]
            temp = t
            j = 0
            while j < len(word) and word[j] in temp:
                temp = temp[word[j]]
                j += 1
                if "*" in temp:
                    sentence[i] = word[:j]
                    break

        return " ".join(sentence)


print(
    Solution().replaceWords(
        dictionary=["a", "aa", "aaa", "aaaa"],
        sentence="a aa a aaaa aaa aaa aaa aaaaaa bbb baba ababa",
    )
)
