from typing import List


class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        last = 0
        count = 0
        for t in target:
            if t > last:
                count += t - last
            last = t
        return count


print(Solution().minNumberOperations([1, 2, 3, 2, 1]))



















print('hihihihihih')
print('hihihihi')
print('gggggggggggggg')
print('runjeeth')
print('rohit')