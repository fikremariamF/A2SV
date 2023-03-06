class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        for val in s:
            # print(stack , val)
            if val == "(":
                stack.append(0)
            else:
                val = max(2 * stack.pop(), 1)
                if stack:
                    stack[-1] += val
                else:
                    stack.append(val)
        return stack[0]