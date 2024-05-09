from typing import List
import math


class Solution:

    def solve(self, value, rows, cols):
        return value // cols, value % cols

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        start = 0
        end = rows * cols - 1
        while start <= end:
            mid = (start + end) // 2
            i, j = self.solve(mid, rows, cols)
            if matrix[i][j] == target:
                return True
            elif target < matrix[i][j]:
                end = mid - 1
            else:
                start = mid + 1
        return False

    # def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    #     start = 0
    #     end = len(matrix)
    #     index = None
    #     while start <= end:
    #         mid = (start + end) // 2
    #         if target >= matrix[mid][0] and target <= matrix[mid][-1]:
    #             index = mid
    #             break
    #         elif target < matrix[mid][0]:
    #             end = mid - 1
    #         else:
    #             start = mid + 1
    #     else:
    #         return False

    #     start = 0
    #     end = len(matrix[index])
    #     while start <= end:
    #         mid = (start + end) // 2
    #         if matrix[index][mid] == target:
    #             return True
    #         elif target < matrix[index][mid]:
    #             end = mid - 1
    #         else:
    #             start = mid + 1
    #     return False


print(Solution().searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 61))
