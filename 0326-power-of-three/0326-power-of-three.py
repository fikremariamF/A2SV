class Solution:
    def checker(self, n):
        if n == 1:
            return True
        elif n % 3 == 0:
            value = self.checker(n/3)
            return value
        else:
            return False
    def isPowerOfThree(self, n: int) -> bool:
        if n == 0:
            return False
        value = self.checker(n)
        return value