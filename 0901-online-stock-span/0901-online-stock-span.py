class StockSpanner:

    def __init__(self):
        self.stack = []
        self.idx = 1
    def next(self, price: int) -> int:
        
        while self.stack and self.stack[-1][0] <= price:
            self.stack.pop()
            
        if not self.stack:
            self.stack.append([price, self.idx])
            self.idx += 1
            return self.idx - 1
        # print(price, self.stack)
        
        # print(self.stack)
        self.stack.append([price, self.idx])
        self.idx += 1
        # print("ans", self.stack[-1][1] - self.stack[-2][1])
        return self.stack[-1][1] - self.stack[-2][1]
            

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)