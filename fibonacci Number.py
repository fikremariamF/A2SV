class Solution:
    def fib(self, n: int) -> int:
        fibonachis = [0,1]
        counter = 2
        if n < 2:
            return fibonachis[n]
        while counter <= n:
            fibonachis.append(fibonachis[0] +fibonachis[1])
            fibonachis.pop(0)
            counter += 1
            
        return fibonachis[-1]
        
        
