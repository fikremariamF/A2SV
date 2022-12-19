# Enter your code here. Read input from STDIN. Print output to STDOUT
input()
array = input().split()
a = set(input().split())
b = set(input().split())
# print(m)
# print(a)
# print(b)

sum = 0
for value in array:
    if value in a:
        # print("+")
        sum += 1
    if value in b:
        # print("-")
        sum -= 1
print(sum)
