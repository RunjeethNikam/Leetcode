from collections import deque
from typing import List


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        board = list(reversed(board))
        n = len(board)

        q = deque([[1, 0]])
        visited = set([1])
        while len(q):
            # position, step = q.popleft()
            item = q.popleft()
            position, step = item[0], item[1]
            _r = (position - 1) // n
            if _r % 2 == 1:
                # odd row
                _c = n -(position - _r * n - 1) - 1
            else:
                _c = position - _r * n - 1
            if board[_r][_c] != -1:
                position = board[_r][_c]
                # q.append([board[_r][_c], step])
            if position == n * n:
                return step
            else:
                for i in range(position + 1, min(position + 6 + 1, n * n + 1)):
                    if i not in visited:
                        q.append([i, step + 1])
                        visited.add(i)

        return -1


print(
    Solution().snakesAndLadders(
        [
            [-1, -1, 19, 10, -1],
            [2, -1, -1, 6, -1],
            [-1, 17, -1, 19, -1],
            [25, -1, 20, -1, -1],
            [-1, -1, -1, -1, 15],
        ]
    )
)
