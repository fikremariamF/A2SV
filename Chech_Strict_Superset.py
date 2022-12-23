# Enter your code here. Read input from STDIN. Print output to STDOUT
def checker():
    super_set = set(map(int, input().split()))
    size_super = len(super_set)
    truth = True
    numberOfSubsets = int(input())
    for iteration in range(numberOfSubsets):
        inp = set(map(int,input().split()))
        if len(inp) == size_super:
            return False
        else:
            for num in inp:
                if num not in super_set:
                    return False
    
    return True

print(checker())
