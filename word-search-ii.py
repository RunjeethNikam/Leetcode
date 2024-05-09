from typing import List


class Solution:
    t = {}
    result = []

    def valid(self, row, col, board):
        return row < len(board) and row >= 0 and col < len(board[0]) and col >= 0

    def solve(self, i, j, curr, board, word, visited):
        if "-" in curr:
            self.result.append(word)

        for row, col in zip([0, 1, 0, -1], [+1, 0, -1, 0]):
            I = i + row
            J = j + col
            if self.valid(I, J, board) and not visited[I][J] and board[I][J] in curr:
                visited[I][J] = True
                self.solve(I, J, curr[board[I][J]], board, word + board[I][J], visited)
                visited[I][J] = False

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.result = []
        for word in words:
            cur = self.t
            for ch in word:
                if ch not in cur:
                    cur[ch] = {}
                cur = cur[ch]
            cur["-"] = {}

        visited = [[False for _ in range(len(board[0]))] for _1 in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                ch = board[i][j]
                if ch in self.t:
                    visited[i][j] = True
                    self.solve(i, j, self.t[ch], board, ch, visited)
                    visited[i][j] = False

        return self.result


print(
    Solution().findWords(
        [["a"]],
        ["ab"],
    )
)
