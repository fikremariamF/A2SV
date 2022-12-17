class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        new_matrix = [[]]*len(matrix[0])
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[0])):
                new_matrix[j] = [*new_matrix[j], matrix[i][j]]
        return new_matrix