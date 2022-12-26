# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
first_input = input().split()
a_length = int(first_input[0])
b_length = int(first_input[1])

d = defaultdict(list)
for index in range(a_length):
    d[input()].append(index + 1)

for index in range(b_length):
    val = d[input()]
    if len(val) == 0:
        print(-1)
        continue
    for i in range(len(val)):
        if i == len(val)-1:
            print(val[i])
        else:
            print(val[i], end=" ")
