if __name__ == '__main__':
    N = int(input())
    valuesList = []
    functions = {
        "append" : lambda value: valuesList.append(value),
        "print" : lambda _: print(valuesList),
        "remove" : lambda value: valuesList.remove(value) if value in valuesList else False,
        "sort" : lambda _: valuesList.sort(),
        "pop" : lambda _: valuesList.pop(),
        "reverse" : lambda _: valuesList.reverse(),
        "insert": lambda index, value: valuesList.insert(index, value)   
    }
    
    
    for order in range(N):
        user_input = input().split()
        # print(user_input)
        if len(user_input) == 3:
            functions[user_input[0]](int(user_input[1]),int(user_input[2]))
        elif len(user_input) == 2:
            functions[user_input[0]](int(user_input[1]))
        else:
            functions[user_input[0]](None)
            
