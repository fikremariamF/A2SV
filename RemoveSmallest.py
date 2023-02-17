iterations = int(input())

for iteration in range(iterations):
    input()
    nums = list(map(int, input().split()))
    nums.sort()
    i = 1
    while i < len(nums):
        if abs(nums[i] - nums[i - 1]) <= 1:
            nums.pop(i - 1)
        else:
            i += 1
    if len(nums) == 1:
        print("YES")
    else:
        print("NO")
