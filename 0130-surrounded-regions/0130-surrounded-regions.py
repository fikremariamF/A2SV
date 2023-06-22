class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        row = len(board)
        col = len(board[0])

        def dfs(i,j):
            board[i][j] = 'T'
            for x, y in [(-1,0), (0,-1), (1,0), (0,1)]:
                temp_x = i+x
                temp_y = j+y
                if(temp_x>=0 and temp_y>=0 and temp_x<row and temp_y<col and board[temp_x][temp_y] == 'O'):
                    print(temp_x,temp_y)
                    dfs(temp_x,temp_y)
        
        for i in range(row):
            if board[i][0] == 'O':
                dfs(i,0)
            if board[i][col-1] == 'O':
                dfs(i,col-1)
        for j in range(col):
            if board[0][j] == 'O':
                dfs(0,j)
            if board[row-1][j] == 'O':
                dfs(row-1,j)
        for i in range(row):
            for j in range(col):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == 'T':
                    board[i][j] = 'O'