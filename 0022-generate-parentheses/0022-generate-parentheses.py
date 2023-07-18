class Solution:
    def generateParenthesis(self, n):
        result = []
        self.generateParentheses(result, "", 0, 0, n)
        return result

    def generateParentheses(self, result, current, open, close, n):
        if len(current) == 2 * n:
            result.append(current)
            return
        if open < n:
            self.generateParentheses(result, current + '(', open + 1, close, n)
        if close < open:
            self.generateParentheses(result, current + ')', open, close + 1, n)

        