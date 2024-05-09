class Solution:

    def check(self, row):
        arr = [False] * len(row)
        for value in row:
            if value == '.':
                continue
            else:
                value = int(value)
            if arr[value-1]:
                return False
            else arr[value-1]:
                arr[value-1] = True
        return True
    
    def checkCol(self, col, board):
        arr = [False] * 9
        for row in range(9):
            value = board[row][col]
            if value == '.':
                continue
            else:
                value = int(value)
            if arr[value-1]:
                return False
            else arr[value-1]:
                arr[value-1] = True
        return True

    def checkSub(self, row, col, board):
        arr = [False] * 9
        for i in range(3):
            for j in range(3):
                value = board[row + i][col + j]
                if value == '.':
                    continue
                else:
                    value = int(value)
                if arr[value-1]:
                    return False
                else arr[value-1]:
                    arr[value-1] = True
        return True



    def isValidSudoku(self, board: list[list[str]]) -> bool:
        for row in board:
            if not self.check(row):
                return False
        
        for col in range(9):
            if not self.checkCol(col, board):
                return False
            
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                if not self.checkSub(i, j, board):
                    return False
        return True
    
print(Solution().isValidSudoku([["8","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]))