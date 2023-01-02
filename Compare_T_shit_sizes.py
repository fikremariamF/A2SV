iterations = int(input())

for iteration in range(iterations):
    order = {"S": 0, "M": 1, "L": 2}
    sizes = list(map(list,input().split()))
    size_0 = sizes[0].pop()
    size_1 = sizes[1].pop()

    if size_0 != size_1:
        if order[size_0] > order[size_1]:
            print(">")
        else:
            print("<")
    else:
        if size_0 == "L":
            if len(sizes[0]) > len(sizes[1]):
                print(">")
            elif len(sizes[0]) < len(sizes[1]):
                print("<")
            else:
                print("=")
        else:
            if len(sizes[0]) < len(sizes[1]):
                print(">")
            elif len(sizes[0]) > len(sizes[1]):
                print("<")
            else:
                print("=")
