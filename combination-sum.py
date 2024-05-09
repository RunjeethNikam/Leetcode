from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        def dfs(candidates, i, target, chosen, sm):
            if sm == target:
                result.append(chosen)
            elif sm < target:
                for index in range(i, len(candidates)):
                    dfs(candidates, index, target, chosen + [candidates[index]], sm + candidates[index])
        dfs(candidates, 0, target, [], 0)
        return result
    
Solution().combinationSum([2,3,6,7], 7)