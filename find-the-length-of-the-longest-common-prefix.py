from typing import List


class Solution:

    def add_prefix(self, s: set, num):
        i = 0
        result = ""
        while i < len(num):
            result += num[i]
            s.add(result)
            i += 1
        return s

    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        arr1 = list(map(lambda _: str(_), arr1))
        arr2 = list(map(lambda _: str(_), arr2))

        s = set()
        for num in arr1:
            s = self.add_prefix(s, num)

        result = 0
        for num in arr2:
            count = 0
            temp = ""
            i = 0
            while i < len(num):
                temp += num[i]
                if temp in s:
                    count += 1
                else:
                    break
                result = max(result, count)
                i += 1
        return result
    
print(Solution().longestCommonPrefix([13,27,45], [21,27,48]))