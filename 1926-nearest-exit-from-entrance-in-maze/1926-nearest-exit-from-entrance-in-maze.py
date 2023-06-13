class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        moves = [[-1,0], [1,0], [0,-1], [0,1]]
        visited = {(entrance[0], entrance[1])}
        queue = deque([[entrance[0], entrance[1], 0]])
        while queue:
            # print(visited)
            xi, yi, dist = queue.popleft()
            # print("in", xi, yi)
            for i,j in moves:
                xj, yj = xi + i, yi + j
                # print("op", xj,yj)
                if 0 <= xj < len(maze) and 0 <= yj < len(maze[0]) and maze[xj][yj] == "." and (xj, yj) not in visited:
                    # print("valid")
                    if 0==xj or xj == len(maze) - 1 or yj == 0 or yj == len(maze[0]) - 1:
                        # print(xj,yj)
                        return dist + 1
                    queue.append([xj,yj, dist + 1])
                    visited.add((xj,yj))
                
        return -1