input()
list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))
ptr1 = 0
ptr2 = 0
output = []
while ptr1 < len(list1) and ptr2 < len(list2):
    if list1[ptr1] < list2[ptr2]:
        output.append(list1[ptr1])
        ptr1 += 1
    else:
        output.append(list2[ptr2])
        ptr2 += 1

output.extend(list1[ptr1:])
output.extend(list2[ptr2:])
print(*output)
