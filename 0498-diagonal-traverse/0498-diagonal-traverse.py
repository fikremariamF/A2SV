class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        output = []
        prev_func = "+"
        row, col = 0, 0
        iterations = len(mat) + len(mat[0])
        for iteration in range(iterations):
            if iteration == 0:
                output.append(mat[0][0])
                if len(mat[0]) > 1:
                    col += 1
                else:
                    row += 1
            else:
                if prev_func == "+":
                    while 0 <= row < len(mat) and 0 <= col < len(mat[0]):
                        output.append(mat[row][col])
                        if col == 0 or row == len(mat)-1:
                            break
                        row += 1
                        col -= 1
                    if row < len(mat) - 1:
                        row += 1
                    else:
                        col += 1
                    prev_func = "-"
                else:
                    while 0 <= row < len(mat) and 0 <= col < len(mat[0]):
                        output.append(mat[row][col])
                        if row == 0 or col == len(mat[0]) -1:
                            break
                        row -= 1
                        col += 1
                        
                    if col < len(mat[0])-1:
                        col += 1
                    else:
                        row += 1
                    prev_func = "+"
        return output
                
            