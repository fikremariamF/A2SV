def swap_case(s):
    mylist = []
    for letter in s:
        if letter.isupper():
            mylist.append(letter.lower())
        elif letter.islower():
            mylist.append(letter.upper())
        else:
            mylist.append(letter)
    # print(mylist)
    return ''.join(mylist)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
