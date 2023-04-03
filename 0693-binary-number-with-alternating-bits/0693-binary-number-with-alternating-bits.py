class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        curr = None
        while n:
            if curr == None:
                curr = (n & (1 << (1 - 1))) >> (1 - 1)
                n >>= 1
            else:
                temp = (n & (1 << (1 - 1))) >> (1 - 1)
                if temp == curr:
                    return False
                curr = temp
                n >>= 1
        return True