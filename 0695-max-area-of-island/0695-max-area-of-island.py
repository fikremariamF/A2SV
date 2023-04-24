class Solution:
    def traverse(self, i, j):
        self.visited.add((i,j))
        paths = [[1,0], [-1,0], [0,1], [0, -1]]
        total = 0
        for path in paths:
            row, col = path[0], path[1]
            row += i
            col += j
            if 0 <= row < len(self.grid) and 0 <= col < len(self.grid[row]) and (row, col) not in self.visited and self.grid[row][col] == 1:
                total += self.traverse(row, col)
                
        return 1 + total
    
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.grid = grid
        max_area = 0
        self.visited = set()
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if (row,col) not in self.visited and self.grid[row][col] == 1:
                    area = self.traverse(row, col)
                    max_area = max(area, max_area)
                    
        return max_area