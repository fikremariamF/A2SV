import textwrap

def wrap(string, max_width):
    string = list(string)
    i = 0
    place = 0
    while i < len(string):
        if max_width == place:
             string.insert(i, "\n")
             place = 1
             i += 1
        else:
            place += 1
        i += 1
    return "".join(string)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
