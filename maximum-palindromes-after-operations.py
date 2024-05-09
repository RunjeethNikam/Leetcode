from typing import List


class Solution:
    def maxPalindromesAfterOperations(self, words: List[str]) -> int:
        a = ord('a')
        f = [0] * 27
        temp = []
        for word in words:
            temp.append(len(word))
            for ch in word:
                f[ord(ch) - a] += 1
        temp.sort()
        even = 0
        odd = 0
        for freq in f:
            even += freq // 2
            odd += freq % 2
        count = 0
        for query in temp:
            if query % 2 == 1:
                if odd >= 1:
                    odd -= 1
                else:
                    odd += 1
                    even -= 1
            if even < query//2:
                break
            even -= query //2
            count += 1
        return count 

print(Solution().maxPalindromesAfterOperations(["a","a","caa"]))