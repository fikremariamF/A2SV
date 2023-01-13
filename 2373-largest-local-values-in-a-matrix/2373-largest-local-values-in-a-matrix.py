class Solution:
    def maxFinder(self, row, col, grid):
        maxVal = 0
        for i in range(row, row + 3):
            for j in range(col, col + 3):
                if grid[i][j] > maxVal:
                    maxVal = grid[i][j]
        return maxVal
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        output = []
        # current = [grid[0][0],grid[1][0]grid[2][0],grid[0][1],grid[1][1]grid[2][1],grid[0][2],grid[1][2]grid[2][2]]
        for row in range(len(grid) - 2):
            maxs = []
            for col in range(len(grid) - 2):
                maxs.append(self.maxFinder(row, col, grid))
            output.append(maxs)
        return output