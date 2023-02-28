class Solution:
    def checker(self, n):
        if n == 1:
            return True
        elif n % 2 == 0:
            value = self.checker(n/2)
            return value
        else:
            return False
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        value = self.checker(n)
        return value