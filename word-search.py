from typing import List


class Solution:
    index: int
    def validate(self, i, j, board):
        return i < len(board) and i >= 0 and j < len(board[0]) and j >= 0

    def dfs(self, i, j, board, word, visited: set):
        if self.index < len(word):
            row = [0, 1, 0, -1]
            col = [+1, 0, -1, 0]
            for r, c in zip(row, col):
                I = i + r
                J = j + c
                if (
                    self.validate(I, J, board)
                    and (I, J) not in visited
                    and word[self.index] == board[I][J]
                ):
                    visited.add((I, J))
                    self.index += 1
                    if self.dfs(I, J, board, word, visited):
                        return True
            self.index -= 1
            visited.discard((i, j))
            return False
        else:
            return True

    # def bfs(self, i, j, board, word):
    #     ng = set()
    #     ng.add((i, j))

    #     visited = set()
    #     visited.add((i, j))

    #     row = [0, 1, 0, -1]
    #     col = [+1, 0, -1, 0]

    #     index = 0

    #     while len(ng):
    #         if index == len(word):
    #             return True

    #         for i, j in ng:
    #             if word[index] == board[i][j]:
    #                 ng.discard((i, j))
    #                 for r, c in zip(row, col):
    #                     I = i + r
    #                     J = j + c
    #                     if self.validate(I, J, board):
    #                         ng.add((I, J))
    #                 index += 1
    #                 break

    #         else:
    #             return False

    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    # self.bfs(i, j, board, word)
                    visited.add((i, j))

                    self.index = 1
                    if self.dfs(i, j, board, word, visited):
                        return True
                    visited.clear()

        return False


print(
    Solution().exist(
        [["A", "B", "C", "E"], ["S", "F", "E", "S"], ["A", "D", "E", "E"]],
        "ABCEFSADEESE",
    )
)
