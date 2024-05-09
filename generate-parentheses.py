from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def dfs(left, right, word):
            if len(word) == n * 2:
                result.append(word)
                return 
            if left < n:
                dfs(left+1, right, word + '(')

            if right < left:
                dfs(left, right+1, word + ')')

        dfs(0, 0, "")
        return result
    
print(Solution().generateParenthesis(3))
