from typing import List


class Solution:
    def get_index(self, arr, i):
        if i< 0:
            return 0
        try:
            return arr[i]
        except IndexError:
            return 0

    def getRow(self, rowIndex: int) -> List[int]:
        l1 = [1]
        i = 0
        while i < rowIndex:
            temp = []
            j = 0
            while j < (len(l1) + 1):
                temp.append(self.get_index(l1, j - 1) + self.get_index(l1, j))
                j += 1
            l1 = temp
            i += 1
        return l1

print(Solution().getRow(5))