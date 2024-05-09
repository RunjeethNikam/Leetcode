from typing import List


class Solution:
    result = []

    def solve(self, nums, comb: list, visited):
        if len(nums) != len(comb):
            for index, value in enumerate(nums):
                if not visited[index]:
                    visited[index] = True
                    comb.append(value)
                    self.solve(nums, comb, visited)
                    comb.pop()
                    visited[index] = False
        else:
            self.result.append(comb[:])

    def permute(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        visited = [False for _ in nums]
        self.solve(nums, [], visited)
        return self.result

# print(Solution().permute([1,2,3]))