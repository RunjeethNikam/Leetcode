from typing import List
from pprint import pprint


class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        for c in range(len(matrix[0])):
            mx = -1
            for r in range(len(matrix)):
                mx = max(mx, matrix[r][c])
            for r in range(len(matrix)):
                if matrix[r][c] == -1:
                    matrix[r][c] = mx
        return matrix
    
pprint(Solution().modifiedMatrix([[1,2,-1],[4,-1,6],[7,8,9]]))
