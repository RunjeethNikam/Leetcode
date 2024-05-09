from typing import List

class Solution:
    result = []

    def solve(self, n, k, comb):
        if k > 0:
            if n >= k:
                for i in range(n, 0, -1):
                    self.solve(i-1, k-1, comb + [i])
        else:
            self.result.append(comb)



    def combine(self, n: int, k: int) -> List[List[int]]:
        self.result = []
        self.solve(n, k, [])
        return self.result
        
print(Solution().combine(13,13))