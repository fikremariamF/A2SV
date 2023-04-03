class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        difference = 0
        while x or y:
            if x & 1 != y & 1:
                difference += 1
            x >>= 1
            y >>= 1
        return difference