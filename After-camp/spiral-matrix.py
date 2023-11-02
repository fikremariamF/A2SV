class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        output = []
        
        prev = "up"
        top_limit, right_limit, bottom_limit, left_limit = 0, len(matrix[0]) - 1, len(matrix) - 1, 0
        i, j = 0,0
        while len(output) < len(matrix) * len(matrix[0]):
            if prev == "up":
                while j <= right_limit:
                    output.append(matrix[i][j])
                    j += 1
                else:
                    j -= 1
                    prev = "right"
                i += 1
                top_limit += 1
            if len(output) >= len(matrix) * len(matrix[0]):
                break
            if prev == "right":
                while i <= bottom_limit: 
                    output.append(matrix[i][j])
                    i += 1
                else:
                    i -= 1
                    prev = "bottom"
                j -= 1
                right_limit -= 1
            if len(output) >= len(matrix) * len(matrix[0]):
                break
            if prev == "bottom":
                while j >= left_limit:
                    output.append(matrix[i][j])
                    j -= 1
                else:
                    j += 1
                    prev = "left"
                i -= 1
                bottom_limit -= 1
            if len(output) >= len(matrix) * len(matrix[0]):
                break
            if prev == "left":
                while i >= top_limit:
                    output.append(matrix[i][j])
                    i -= 1
                else:
                    i += 1
                    prev = "up"
                
                j += 1
                left_limit += 1
            if len(output) >= len(matrix) * len(matrix[0]):
                break
        return output