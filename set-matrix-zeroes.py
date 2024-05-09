class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        row_0_has_zero = False
        col_0_has_zero = False
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                value = matrix[i][j]
                if value == 0:
                    if i == 0:
                        row_0_has_zero = True
                    if j == 0:
                        col_0_has_zero = True
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        if row_0_has_zero:
            for i in range(len(matrix[0])):
                matrix[0][i] = 0

        if col_0_has_zero:
            for i in range(len(matrix)):
                matrix[i][0] = 0
        return matrix
    
print(Solution().setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]]))
        