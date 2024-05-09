class Solution:
    def totalNQueens(self, n: int) -> int:
        count = 0

        def get_forward(i, j):
            return (i - min(i, j), j - min(i, j))

        def get_backward(i, j):
            while i < (n-1) and j > 0:
                i += 1
                j -= 1
            return (i, j)

        def solve(knight_left, row, A: set, B: set, C: set, D: set):
            nonlocal count
            if knight_left > 0 and row not in A and row < n:
                for col in range(n):
                    if (
                        (col not in B)
                        and get_forward(row, col) not in C
                        and get_backward(row, col) not in D
                    ):
                        A.add(row)
                        B.add(col)
                        C.add(get_forward(row, col))
                        D.add(get_backward(row, col))
                        solve(knight_left - 1, row + 1, A, B, C, D)
                        A.remove(row)
                        B.remove(col)
                        C.remove(get_forward(row, col))
                        D.remove(get_backward(row, col))

            elif knight_left == 0:
                count += 1

        for i in range(n):
            solve(
                n - 1,
                1,
                set([0]),
                set([i]),
                set([get_forward(0, i)]),
                set([get_backward(0, i)])
            )

        return count


print(Solution().totalNQueens(4))
