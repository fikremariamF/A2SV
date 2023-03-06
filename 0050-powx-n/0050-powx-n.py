class Solution:
    def power(self,x,n):
        if n == 0:
            return 1
        elif n == 1:
            return x
        elif n % 2 == 0:
            return self.power(x*x, n/2)
        else:
            return x * self.power(x*x, (n-1)/2)
        
    def myPow(self, x: float, n: int) -> float:
        return self.power(x,n) if n >= 0 else 1/self.power(x,-n)
    