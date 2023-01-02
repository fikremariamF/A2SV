iterations = int(input())

for iteration in range(iterations):
    items = int(input())
    int_arr = list(map(int, input().split()))
    word = list(input())
    int_letter_dict = {}
    answer = "Yes"
    for iter in range(items):
        if int_arr[iter] in int_letter_dict:
            if int_letter_dict[int_arr[iter]] != word[iter]:
                answer = "NO"
        else:
            int_letter_dict[int_arr[iter]] = word[iter]
    print(answer)
