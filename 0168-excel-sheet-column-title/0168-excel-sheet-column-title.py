class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        
        if columnNumber < 27:
            return chr(columnNumber + 64)
        else:
            output = []
            while columnNumber > 26:
                output.append((columnNumber) % 26)
                if columnNumber / 26 == columnNumber // 26:
                    columnNumber = (columnNumber -1) // 26
                else:
                    columnNumber = (columnNumber) // 26
            output.append(columnNumber)
            ouput = output.reverse()
            for idx in range(len(output)):
                if output[idx] == 0:
                    output[idx]= chr(26 + 64)
                else:
                    output[idx]= chr(output[idx] + 64)
            return "".join(output)