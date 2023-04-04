tests = int(input())
 
def checker(num):
    if num == 1:
        print(3)
        return
    for i in range(1, 32):
        if (2 ** i) == num:
            print(num + 1)
            return
 
    for i in range(64):
        if (num >> i & 1) == 1:
            print(2**i)
            return
 
for i in range(tests):
    num = int(input())
    checker(num)
