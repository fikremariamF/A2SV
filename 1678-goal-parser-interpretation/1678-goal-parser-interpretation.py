class Solution:
    def interpret(self, command: str) -> str:
        returnList = []
        i = 0
        while i < len(command):
            if command[i] == "G":
                returnList.append("G")
                i += 1
            elif command[i] == "(":
                if command[i+1] == ")":
                    returnList.append("o")
                    i += 2
                else:
                    returnList.append("al")
                    i += 4
        return ''.join(returnList)
                