class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        length = len(grid)
        
        if grid[0][0] == 1 or grid[len(grid)-1][len(grid)-1] == 1:
            return -1
        
        moves = [[1,0], [-1,0], [0,1], [0,-1], [-1,-1], [1,1], [1,-1], [-1,1]]
        
        paths = deque([[0, 0, 1]])
        
        visited = set()
        
        visited.add((0,0))
        
        while paths and paths[0]:
            i,j, dist = paths.popleft()
            
            if i == length - 1 and j == length - 1:
                return dist
                
            for x, y in moves:
                xi, yj = x + i, y + j
                
                if 0 <= xi < length and 0 <= yj < length:
                    if (xi, yj) not in visited and grid[xi][yj] == 0:
                        paths.append([xi, yj, dist + 1])
                        visited.add((xi,yj))
        
        return -1