class Solution:
    # def rotator
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        output = [[] for _ in range(len(matrix))]
        for row in range(len(matrix)- 1, -1, -1):
            for idx in range(len(matrix)):
                output[idx].append(matrix[row][idx])
                # col += 1
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                matrix[row][col] = output[row][col]
            
    
            