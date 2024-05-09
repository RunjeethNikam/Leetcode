# class WordDictionary:

#     def __init__(self):
#         # self.t = {}
        

#     def addWord(self, word: str) -> None:
#         # curr = self.t
#         # for i in word:
#         #     if i not in curr:
#         #         curr[i] = {}
#         #     curr = curr[i]
#         # curr['-'] = {}
    
#     def dfs(self, curr, word, i):
#         if i < len(word):
#             if word[i] != '.':
#                 if word[i] not in curr:
#                     return False
#                 return self.dfs(curr[word[i]], word, i+1)
#             else:
#                 for _, value in curr.items():
#                     if self.dfs(value, word, i+1):
#                         return True
#                 return False
#         return '-' in curr
        

#     def search(self, word: str) -> bool:
#         return self.dfs(self.t, word, i=0)
        


# # Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# for i in ['a', 'a']:
#     obj.addWord(i)
# print(obj.search('a.'))
# # print(obj.search('dad'))
# # print(obj.search('.ad'))
# # print(obj.search('b..'))

from string import ascii_lowercase

class WordDictionary:

    def __init__(self):
        self.s = set()
        

    def addWord(self, word: str) -> None:
        self.s.add(word)

    def get_index(word):
        result = []
        for index, value in enumerate(word):
            if value == '.':
                result.append(index)
        return result

        

    def search(self, word: str) -> bool:
        indexes: list = self.get_index(word)
        def safe_list_get (l, idx, default):
            try:
                return l[idx]
            except IndexError:
                return default
        i, j = safe_list_get(indexes, 0, None), safe_list_get(indexes, 1, None)
        if i is None and j in None:
            return word in self.s
        elif i is not None and j is not None:
            for a1 in ascii_lowercase:
                for a2 in ascii_lowercase:
                    newWord = word[:i] + a1 + word[i+1, j] + a2 + word[j+1:]
                    if newWord in self.s:
                        return True
        else:
            for a1 in ascii_lowercase:
                newWord = word[:i] + a1 + word[i+1:]
                if newWord in self.s:
                    return True
        return False
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)