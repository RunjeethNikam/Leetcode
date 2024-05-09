class Solution:

    def swap(self, matrix, row, increment):
        temp = matrix[0 + row][0 + row + increment]
        ln = len(matrix) - 1


        matrix[0 + row][0 + row + increment] = matrix[ln - row - increment][0 + row]
        matrix[ln - row - increment][0 + row] = matrix[ln - row][ln - row - increment]
        matrix[ln - row][ln - row - increment] = matrix[0 + row + increment][ln - row]
        matrix[0 + row + increment][ln - row] = temp

        


    def rotateRow(self, matrix, row):
        for index, value in enumerate(range(row, len(matrix) - row - 1)):
            self.swap(matrix, row, index)

    def rotate(self, matrix: list[list[int]]) -> None:
        for i in range(0, (len(matrix) //2)):
            self.rotateRow(matrix, i)

print(Solution().rotate([[1,2,3],[4,5,6],[7,8,9]]))
        