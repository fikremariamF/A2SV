class Solution:
    def checkWinner(self, x_pos, o_pos, board):
        winners = set()
        for row in board:
            prev = row[0]
            for col in range(1,len(row)):
                if row[col] != prev:
                    break
                else:
                    if col == 2:
                        if row[col] == prev:
                            if prev != " ":
                                winners.add(prev)
        for col in range(3):
            prev = board[0][col]
            for row in range(1,3):
                if prev != board[row][col]:
                    break
                else:
                    if row == 2:
                        if board[row][col] == prev:
                            if prev != " ":
                                winners.add(prev)
        # print(winners)
        if board[0][0] == board[1][1] == board[2][2]:
            if board[0][0] != " ":
                winners.add(board[0][0])
        elif board[0][2] == board[1][1] == board[2][0]:
            if board[1][1] != " ":
                winners.add(board[1][1])
        return winners
                
    def validTicTacToe(self, board: List[str]) -> bool:
        newBoard = [ [], [], []]
        Xs = []
        Os = []
        x_Os= []
        for row in range(3):
            for col in range(3):
                newBoard[row].append(board[row][col])
                if board[row][col] != " ":
                    x_Os.append(board[row][col])
                    if board[row][col] == "X":
                        Xs.append([row, col])
                    else:
                        Os.append([row, col])
        board = newBoard[:]
        # print(board)
        # print(Xs, Os)
        x_Os = Counter(x_Os)
        if x_Os["X"] == x_Os["O"] or x_Os["X"] == x_Os["O"] + 1:
            x_count = x_Os["X"] 
            # o_count = x_Os["O"]
            if x_count >= 3:
                winners = list(self.checkWinner(Xs, Os, board))
                # print(winners)
                if len(winners) == 0 or (winners[0] == "X" and x_Os["X"] == x_Os["O"] + 1) or (winners[0] == "O" and x_Os["X"] == x_Os["O"]):
                    if len(winners) == 1 or len(winners) == 0:
                        return True
                else:
                    False
            else:
                return True
        else:
            return False