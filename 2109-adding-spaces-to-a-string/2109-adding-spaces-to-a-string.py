class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        index = 0
        length = len(s)
        pos = 0
        string_list = []
        spaces.append(0)
        while index < len(s):
            if pos < len(spaces):
                if spaces[pos] <= index:
                    string_list.append(" ")
                    pos += 1
                    if pos == len(spaces) - 1:
                        pos += 1
                else:
                    string_list.append(s[index])
                    index += 1
            else:
                string_list.append(s[index])
                index += 1
        return "".join(string_list)
        