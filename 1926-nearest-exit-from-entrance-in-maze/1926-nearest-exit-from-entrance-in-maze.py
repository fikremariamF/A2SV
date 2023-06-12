class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        ROWS, COLS = len(maze), len(maze[0])
        visited = set()
        queue = deque()
        queue.append((tuple(entrance), 0))
        
        while queue:
            element = queue.popleft()
            
            position = element[0]
            step = element[1]
            
            # Check if this position is invalid.
            if (position[0] < 0 or position[0] > ROWS-1
                or position[1] < 0 or position[1] > COLS-1
                or position in visited or maze[position[0]][position[1]] == '+'):
                continue
            
            # Check if this position is the answer.
            if (position[0] == 0 or position[0] == ROWS-1
                or position[1] == 0 or position[1] == COLS-1):
                if step != 0 :
                    return step
            visited.add(position) 
            queue.append(((position[0]+1, position[1]), step+1))
            queue.append(((position[0], position[1]+1), step+1))
            queue.append(((position[0]-1, position[1]), step+1))
            queue.append(((position[0], position[1]-1), step+1))

        return -1