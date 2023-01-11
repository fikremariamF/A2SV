class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        output = []
        
        prev = "up"
        top_limit, right_limit, bottom_limit, left_limit = 0, len(matrix[0]) - 1, len(matrix) - 1, 0
        # print(top_limit, right_limit, bottom_limit, left_limit)
        i, j = 0,0
        while len(output) < len(matrix) * len(matrix[0]):
            # print("in")
            if prev == "up":
                # print(prev)
                # print(i,j)
                while j <= right_limit:
                    # print(matrix[i][j])
                    output.append(matrix[i][j])
                    j += 1
                else:
                    j -= 1
                    prev = "right"
                i += 1
                top_limit += 1
            if len(output) >= len(matrix) * len(matrix[0]):
                break
            # print(output)
            if prev == "right":
                # print(prev)
                # print(i,j)
                while i <= bottom_limit: 
                    # print(i)
                    output.append(matrix[i][j])
                    i += 1
                else:
                    i -= 1
                    prev = "bottom"
                j -= 1
                right_limit -= 1
            if len(output) >= len(matrix) * len(matrix[0]):
                break
            # print(output)
            if prev == "bottom":
                # print(prev)
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
            # print(output)
            if prev == "left":
                # print(prev)
                # print(i,j)
                while i >= top_limit:
                    # print(i,j)
                    output.append(matrix[i][j])
                    i -= 1
                else:
                    i += 1
                    prev = "up"
                
                j += 1
                left_limit += 1
            if len(output) >= len(matrix) * len(matrix[0]):
                break
            # print(output)
            # print(len(output) , len(matrix) * len(matrix[0]))
        return output
                    