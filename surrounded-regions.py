from typing import List


class Solution:
    def is_bordered(self, i, j, grid) -> bool:
        return (
            (i - 1) < 0
            or (i + 1) >= len(grid)
            or (j - 1) < 0
            or (j + 1) >= len(grid[0])
        )

    def dfs(self, i, j, grid):
        if grid[i][j] == "O":
            grid[i][j] = "S"
            # top
            if (i - 1) >= 0 and grid[i - 1][j] == "O":
                self.dfs(i - 1, j, grid)
            # down
            if (i + 1) < len(grid) and grid[i + 1][j] == "O":
                self.dfs(i + 1, j, grid)
            # Right
            if (j + 1) < len(grid[0]) and grid[i][j + 1] == "O":
                self.dfs(i, j + 1, grid)
            # Left
            if (j - 1) >= 0 and grid[i][j - 1] == "O":
                self.dfs(i, j - 1, grid)

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # is_secured = [[False for _ in range(len(board[0]))] for _ in range(len(grid))]
        # visited = [[False for _ in range(len(board[0]))] for _ in range(len(grid))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O" and self.is_bordered(i, j, board):
                    self.dfs(i, j, board)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O":
                    board[i][j] = "X"
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "S":
                    board[i][j] = "O"
        return board
