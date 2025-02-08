from typing import List
from collections import defaultdict



class neighborSum:

    def __init__(self, grid: List[List[int]]):
        self.g = grid
        self.dp = dict()
        rows = len(grid)
        cols = len(grid[0])
        for i in range(rows):
            for j in range(cols):
                self.dp[grid[i][j]] = (i,j)
        

    def adjacentSum(self, value: int) -> int:
        d = [
            (1,0),
            (0,1),
            (-1,0),
            (0,-1)
        ]
        sm = 0
        i,j = self.dp[value]
        for I,J in d:
            sm += self.g[I + i][J + j]
        return sm
        

    def diagonalSum(self, value: int) -> int:
        d = [
            (1,1),
            (-1,-1),
            (-1,1),
            (1,-1)
        ]
        sm = 0
        i,j = self.dp[value]
        for I,J in d:
            sm += self.g[I + i][J + j]
        return sm
        


# Your neighborSum object will be instantiated and called as such:
# obj = neighborSum(grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)