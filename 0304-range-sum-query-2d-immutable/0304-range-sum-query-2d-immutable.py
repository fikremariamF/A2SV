class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        for row in range(len(matrix)):
            for idx in range(1,len(matrix[row])):
                matrix[row][idx] += matrix[row][idx-1]
        for row in range(1,len(matrix)):
            for idx in range(len(matrix[row])):
                matrix[row][idx] += matrix[row-1][idx]
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if row1 == 0 and col1 == 0:
            return self.matrix[row2][col2]
        elif row1 == 0:
            return self.matrix[row2][col2] - self.matrix[row2][col1-1]
        elif col1 == 0:
            return self.matrix[row2][col2] - self.matrix[row1-1][col2]
        return self.matrix[row2][col2] - self.matrix[row1-1][col2] - self.matrix[row2][col1-1] + self.matrix[row1-1][col1-1]
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)