class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return

        m, n = len(board), len(board[0])

        def markBorderConnectedO(row, col):
            if row < 0 or row >= m or col < 0 or col >= n or board[row][col] != 'O':
                return
            board[row][col] = 'B'
            markBorderConnectedO(row + 1, col)
            markBorderConnectedO(row - 1, col)
            markBorderConnectedO(row, col + 1)
            markBorderConnectedO(row, col - 1)

        for i in range(m):
            markBorderConnectedO(i, 0)
            markBorderConnectedO(i, n - 1)
        for j in range(n):
            markBorderConnectedO(0, j)
            markBorderConnectedO(m - 1, j)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'B':
                    board[i][j] = 'O'