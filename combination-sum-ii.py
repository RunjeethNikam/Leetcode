from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = list()
        temp = []

        def solve(index, target):
            nonlocal result
            nonlocal temp

            if target == 0:
                result.append(temp[:])
                return

            if index < len(candidates) and target > 0:
                solve(index + 1, target)
                if not temp or candidates[index] != temp[-1]:
                    temp.append(candidates[index])
                    solve(index + 1, target - candidates[index])
                    temp.pop()

        solve(0, target)
        return list(result)


print(Solution().combinationSum2(candidates=[2, 5, 2, 1, 2], target=5))
