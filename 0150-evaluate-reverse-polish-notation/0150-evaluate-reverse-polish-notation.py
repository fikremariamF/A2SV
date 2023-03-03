class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = {"+", "-", "*", "/"}
        for char in tokens:
            if char not in operations:
                stack.append(char)
            else:
                if char == "/":
                    temp = float(stack.pop()) 
                    stack.append(int(stack.pop()) / temp )
                elif char == "+":
                    stack.append(int(stack.pop()) + int(stack.pop()))
                elif char == "*":
                    stack.append(int(stack.pop()) * int(stack.pop()))
                else:
                    temp = int(stack.pop())
                    stack.append(int(stack.pop()) - temp )
        return int(stack.pop())