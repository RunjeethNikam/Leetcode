class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        dp = {}

        def check(r, c, n):
            return r >= 0 and c >= 0 and r < n and c < n

        def solve(n, k, r, c):
            if check(r, c, n):
                if (r, c, k) in dp:
                    return dp[(r, c, k)]
                if k == 0:
                    return 1
                else:
                    moves = [
                        (-1, -2),
                        (-2, -1),
                        (-2, +1),
                        (-1, +2),
                        (+1, +2),
                        (+2, +1),
                        (+2, -1),
                        (+1, -2),
                    ]
                    t = 0
                    for ir, ic in moves:
                        t += solve(n, k - 1, r + ir, c + ic)
                    dp[(r, c, k)] = t
                    return dp[(r, c, k)]
            return 0

        f = solve(n, k, row, column)
        return f / (8 ** k)


print(Solution().knightProbability(3, 2, 0, 0))
