from typing import List



class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        p = 1
        for row in grid:
            for value in row:
                p = (p % 12345 * value % 12345) % 12345
        result = [[1] * len(grid[0]) for _ in grid]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                result[i][j] = ((p % 12345) // (grid[i][j] % 12345)) % 12345
        return result
    

print(Solution().constructProductMatrix([[12345],[2],[1]]))
