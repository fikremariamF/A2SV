class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        code = "\n".join(source)
        single_line_comment = False
        multiple_line_comment = False
        charachters = ""
        length = len(code)
        index = 0
        # print(code)
        while index < length:
            # print(code[index])
            # print(single_line_comment)
            # print(multiple_line_comment)
            if single_line_comment:
                if code[index] == "\n":
                    single_line_comment = False
            elif multiple_line_comment:
                if index < length - 1 and code[index] == "*" and code[index + 1] == "/":
                    multiple_line_comment = False
                    index += 2
                    # if index < length - 1 and  code[index + 1] == "\n":
                    #     index += 1
            if not multiple_line_comment and not single_line_comment and code[index] == "/" and code[index + 1] == "*":
                multiple_line_comment = True
                index += 1
            elif not single_line_comment and not multiple_line_comment and code[index] == "/" and code[index + 1] == "/":
                single_line_comment = True
            elif not single_line_comment and not multiple_line_comment:
                charachters = charachters + code[index]
            index += 1
        characters = charachters.split("\n")
        i = 0
        while i < len(characters):
            if characters[i] == "":
                characters.pop(i)
            else:
                i += 1
        # for i in range(len(characters)):
        #     if characters[i][0] == " " and characters[i][1] == " ":
        #         characters[i]= characters[i][2:]
        #         characters.insert(i, "  ")
        return characters
                    