class MinStack:

    def __init__(self):
        self.stack = []
        # self.min = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        # if len(self.stack) == 0:
        #     self.min.append(x)
        # else:
        #     if 
    def pop(self) -> None:
        if len(self.stack) > 0:
            x = self.stack.pop()
            return x
        else:
            return None

    def top(self) -> int:
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            return None

    def getMin(self) -> int:
        return min(self.stack)

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
