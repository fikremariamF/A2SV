class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        DIRECTIONS = {
            1: [(0, -1), (0, 1)],
            2: [(-1, 0), (1, 0)],
            3: [(0, -1), (1, 0)],
            4: [(0, 1), (1, 0)],
            5: [(0, -1), (-1, 0)],
            6: [(0, 1), (-1, 0)]
        }
        
        ROWS, COLS = len(grid), len(grid[0])
        
        def isValidMove(r,c): 
            return r < ROWS and r >= 0 and c < COLS and c >= 0
        
        
        curr = [0,0]
        visited = {(0,0)}
        
        def traverse(x,y):
            # print(x,y, ROWS, COLS)
            if (x,y) == (ROWS - 1, COLS - 1):
                return True
            value = False
            moves = DIRECTIONS[grid[x][y]]
            xi,yi = x + moves[0][0], y + moves[0][1]
            xj,yj = x + moves[1][0], y + moves[1][1]
            
            if (x,y) != (0,0):
                # print(isValidMove(xi,yi), isValidMove(xj,yj))
                if isValidMove(xi,yi) and isValidMove(xj,yj):
                    if (xi,yi) in visited:
                        if (moves[1][0] * -1, moves[1][1] * -1) in DIRECTIONS[grid[xj][yj]] and (xj,yj) not in visited:
                            visited.add((xj,yj))
                            value =  traverse(xj,yj)
                    elif (xj,yj) in visited and (xi,yi) not in visited:
                        if (moves[0][0] * -1, moves[0][1] * -1) in DIRECTIONS[grid[xi][yi]]:
                            visited.add((xi,yi))
                            return traverse(xi,yi)
                else:
                    # print(xi,yi,xj,yj, moves)
                    return False
            else:
                if isValidMove(xi,yi):
                    if (moves[0][0] * -1, moves[0][1] * -1) in DIRECTIONS[grid[xi][yi]]:
                        visited.add((xi,yi))
                        if traverse(xi,yi):
                            value = True
                if (xj, yj) not in visited and isValidMove(xj,yj) and (moves[1][0] * -1, moves[1][1] * -1) in DIRECTIONS[grid[xj][yj]]:
                    visited.add((xj,yj))
                    if traverse(xj,yj):
                        value = True
            return value
        return traverse(0,0)
        