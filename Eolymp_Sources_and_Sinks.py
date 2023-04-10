lines = int(input())
matrix = []
for line in range(lines):
    # print(input())
    row = list(map(int, input().split()))
    matrix.append(row)

sources = []
sinks = []
for idx in range(len(matrix)):
    if 1 not in matrix[idx]:
        sinks.append(idx + 1)

for col in range(len(matrix)):
    items = 0
    for row in range(len(matrix)):
        if matrix[row][col] == 1:
            items = 1
    if items == 0:
        sources.append(col + 1)

sources.sort()
sinks.sort()
print(len(sources), *sources)
print(len(sinks), * sinks)

