class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        prefix_grid= []
        for array in grid:
            prefix_array = []
            for value in array:
                if prefix_array:
                    prefix_array.append(prefix_array[-1] + value)
                else:
                    prefix_array.append(value)
            prefix_grid.append(prefix_array)
        max_val = float("-inf")
        for i in range(len(grid)-2):
            for j in range(2,len(grid[i])):
                sum = prefix_grid[i][j] + prefix_grid[i + 2][j]
                if j - 3 >= 0:
                    sum -= prefix_grid[i][j-3] + prefix_grid[i + 2][j-3]
                sum += grid[i+1][j-1]
                max_val = max(sum,max_val)
        return max_val