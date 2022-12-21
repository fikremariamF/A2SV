class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def strtonumConverter(val):
            numDict = {str(num):num for num in range(10)}
            number = 0
            for i in val:
                number = number * 10 + numDict[i]
            return number
        return str(strtonumConverter(num1) * strtonumConverter(num2))
                
            