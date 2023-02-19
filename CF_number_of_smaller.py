input()
list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))
ptr1 = 0
ptr2 = 0
output = []
while ptr1 < len(list1) and ptr2 < len(list2):
    if list1[ptr1] < list2[ptr2]:
        ptr1 += 1
    else:
        output.append(ptr1)
        ptr2 += 1
if ptr1 == len(list1):
    while len(output) < len(list2):
        output.append(ptr1)
else:
    while len(output) < len(list2):
        output.append(0)
print(*output)
