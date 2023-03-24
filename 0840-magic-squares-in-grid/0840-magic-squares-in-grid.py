class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def checker(row, col):
            result = False
            diag1 = grid[row][col] + grid[row + 1][col + 1] + grid[row + 2][col + 2]
            diag2 = grid[row][col + 2] + grid[row + 1][col + 1] + grid[row + 2][col]
            row1 = grid[row][col] + grid[row][col + 1] + grid[row][col + 2]
            row2 = grid[row + 1][col] + grid[row + 1][col + 1] + grid[row + 1][col + 2]
            row3 = grid[row + 2][col] + grid[row + 2][col + 1] + grid[row + 2][col + 2]
            col1 = grid[row][col] + grid[row + 1][col] + grid[row + 2][col]
            col2 = grid[row][col + 1] + grid[row + 1][col + 1] + grid[row + 2][col + 1]
            col3 = grid[row][col + 2] + grid[row + 1][col + 2] + grid[row + 2][col + 2]
            if diag1 == diag2 == row1 == row2 == row3 == col1 == col2 == col3 :
                result = True
            if not result:
                return False
            
            nums = set()
            for i in range(row,row + 3):
                for j in range(col,col + 3):
                    nums.add(grid[i][j])
            for num in nums:
                if 0 < num < 10:
                    continue
                else:
                    return False
            length = len(nums)
            if length == 9:
                return True
            return False
        
        count = 0
        for row in range(len(grid)-2):
            for col in range(len(grid[row]) - 2):
                val = checker(row,col)
                if val:
                    count += 1
                    
        return count