lines = int(input())
matrix = []
for line in range(lines):
    # print(input())
    row = list(map(int, input().split()))
    matrix.append(row)

paths = set()
for row in range(lines):
    for col in range(lines):
        # print(matrix[row][col], matrix[col][row])
        if matrix[row][col] == 1 and tuple([row, col]) not in paths and tuple([col, row]) not in paths:
            paths.add(tuple([row, col]))

print(len(paths))
