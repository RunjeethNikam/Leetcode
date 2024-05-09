class Solution:
    def get_next_value(self, i, j, board):
        top_left = 0
        top = 0
        top_right = 0
        right = 0
        bottom_right = 0 
        bottom = 0
        bottom_left = 0
        left = 0

        if (i-1) >= 0 and (j-1) >= 0:
            top_left = board[i-1][j-1]
        if (i-1) >= 0:
            top = board[i-1][j]
        if (i-1) >= 0 and (j+1) < len(board[0]):
            top_right = board[i-1][j+1]
        if (j+1) < len(board[0]):
            right = board[i][j+1]
        if (i+1) < len(board) and (j+1) < len(board[0]):
            bottom_right = board[i+1][j+1]
        if (i+1) < len(board):
            bottom = board[i+1][j]
        if (i+1) < len(board) and (j-1) >= 0:
            bottom_left = board[i+1][j-1]
        if (j-1) >= 0:
            left = board[i][j-1]
        count = top_left + top + top_right + right + bottom_right + bottom + bottom_left + left
        if board[i][j] == 1:
            if count < 2:
                return 0
            if count == 2 or count == 3:
                return 1
            if count > 3:
                return 0
            assert 0, "error 1"
        else:
            if count == 3:
                return 1
            else:
                return 0


    def gameOfLife(self, board: list[list[int]]) -> None:
        temp = [ [0] * len(board[0]) for _ in range(len(board)) ]
        for i in range(len(board)):
            for j in range(len(board[0])):
                temp[i][j] = self.get_next_value(i, j, board)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j] = temp[i][j]


board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
Solution().gameOfLife(board)
print(board)