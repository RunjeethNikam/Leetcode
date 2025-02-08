from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        row = 0
        col = cols - 1

        while row < rows and col >= 0:
            value = matrix[row][col]
            if value == target:
                return True
            elif value > target:
                col -= 1
            else:
                row += 1
        return False


print(
    Solution().searchMatrix(
        [
            [1, 4, 7, 11, 15],
            [2, 5, 8, 12, 19],
            [3, 6, 9, 16, 22],
            [10, 13, 14, 17, 24],
            [18, 21, 23, 26, 30],
        ],
        18,
    )
)
