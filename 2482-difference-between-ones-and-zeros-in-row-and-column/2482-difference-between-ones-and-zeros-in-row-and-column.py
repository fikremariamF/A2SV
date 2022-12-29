class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        onesRow = []
        zerosRow = []
        for row in grid:
            ones = 0
            zeros = 0
            for element in row:
                if element == 0:
                    zeros += 1
                else:
                    ones += 1
            onesRow.append(ones)
            zerosRow.append(zeros)
        onesCol = []
        zerosCol = []
        for column in range(len(grid[0])):
            zeros = 0
            ones = 0
            for row in range(len(grid)):
                if grid[row][column] == 0:
                    zeros += 1
                else:
                    ones += 1
            onesCol.append(ones)
            zerosCol.append(zeros)
        for row_index in range(len(grid)):
            for col_index in range(len(grid[row_index])):
                grid[row_index][col_index] = onesRow[row_index] + onesCol[col_index] - zerosRow[row_index] - zerosCol[col_index]
        return grid
                    
                
            
        