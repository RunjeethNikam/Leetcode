from collections import defaultdict

# class Node:
#     val: str
#     ng: list['Node']

#     def __init__(self, val, ng = []) -> None:
#         self.val = val
#         self.ng = ng


# class Trie:
#     def __init__(self):
#         self.t = Node('*', [])

#     def insert(self, word: str) -> None:
#         i = 0
#         temp = self.t
#         while i< len(word) and temp:
#             for ng in temp.ng:
#                 if ng.val == word[i]:
#                     temp = ng
#                     i += 1
#                     break
#             else:
#                 node = Node(word[i], [])
#                 i += 1
#                 temp.ng.append(node)
#                 temp = node
#         temp.ng.append(Node('-', []))
            

#     def search(self, word: str) -> bool:
#         i = 0
#         temp = self.t
#         while i < len(word) and temp:

#             for ng in temp.ng:
#                 if ng.val == word[i]:
#                     temp = ng
#                     i += 1
#                     break
#             else:
#                 return False
#         for ng in temp.ng:
#             if ng.val == '-':
#                 return True   
#         return False


#     def startsWith(self, word: str) -> bool:
#         i = 0
#         temp = self.t
#         while i < len(word) and temp:

#             for ng in temp.ng:
#                 if ng.val == word[i]:
#                     temp = ng
#                     i += 1
#                     break
#             else:
#                 return False
#         return True



class Trie:
    def __init__(self):
        self.t = dict()

    def insert(self, word: str) -> None:
        curr = self.t
        for i in word:
            if i not in curr:
                curr[i] = {}
            curr = curr[i]
        curr['-'] = {}
        

    def search(self, word: str) -> bool:
        cur = self.t
        for i in word:
            if i not in cur:
                return False
            cur = cur[i]
        return '-' in cur

    def startsWith(self, word: str) -> bool:
        cur = self.t
        for i in word:
            if i not in cur:
                return False
            cur = cur[i]
        return True


# # Your Trie object will be instantiated and called as such:



obj = Trie()
obj.insert("apple")
print(obj.search("apple"))
print(obj.search("app"))
print(obj.startsWith("app"))
# print(obj.startsWith("app"))
# obj.insert("app")
# print(obj.search("app"))
