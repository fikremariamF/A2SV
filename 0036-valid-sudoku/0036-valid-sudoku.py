import numpy as np
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        board = np.array(board)
        for row in range(9):
            for col in range(9):
                elm = board[row][col]
                if elm != ".":
                    temprow = board[row][:]
                    for i in range(9):
                        if i != col:
                            if elm == temprow[i]:
                                return False
                    tempcol = board[:,col]
                    # print(elm)
                    # print(tempcol)
                    for i in range(9):
                            if i != row:
                                if elm == tempcol[i]:
                                    # print(elm, tempcol[i])
                                    return False
        print("GOT HERE")
        for row in range(0,9,3):
            # print(row)
            for col in range(0,9,3):
                # print(col)
                tempElements = []
                for i in range(3):
                    for j in range(3):
                        if board[row + i][col +j] != ".":
                            tempElements.append(board[row + i][col +j])
                # print(tempElements)
                if len(tempElements) != len(set(tempElements)):
                    return False
        return True
                        
