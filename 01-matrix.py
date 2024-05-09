from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        r = len(mat)
        c = len(mat[0])
        check = lambda i, j: i >= 0 and i < len(mat) and j >= 0 and j < len(mat[0])
        for i in range(r):
            for j in range(c):
                if mat[i][j] != 0:
                    top = mat[i - 1][j] if check(i - 1, j) else float("inf")
                    left = mat[i][j - 1] if check(i, j - 1) else float("inf")
                    mat[i][j] = min(top + 1, left + 1)

        for i in range(r - 1, -1, -1):
            for j in range(c - 1, -1, -1):
                if mat[i][j] != 0:
                    bottom = mat[i + 1][j] if check(i + 1, j) else float("inf")
                    right = mat[i][j + 1] if check(i, j + 1) else float("inf")
                    mat[i][j] = min(mat[i][j], bottom + 1, right + 1)
        return mat


print(Solution().updateMatrix([[0, 0, 0], [0, 1, 0], [1, 1, 1]]))
