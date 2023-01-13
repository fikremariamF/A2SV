class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        grad_dict = dict()
        
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                # print(grad_dict)
                if grad_dict.get(row - col, -1) != -1:
                    # print(grad_dict[row - col], matrix[row][col])
                    if grad_dict[row - col] != (matrix[row][col]):
                        return False
                else:
                    grad_dict[row - col] = (matrix[row][col])
        
        return True