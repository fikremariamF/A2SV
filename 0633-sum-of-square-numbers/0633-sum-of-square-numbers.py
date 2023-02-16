class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        sqrrt = int(math.sqrt(c))
        left, right = 0, sqrrt
        while left <= right:
            # print(left, right)
            # print((left**2) + (right**2))
            if left**2 + right**2 > c:
                right -= 1
            elif left**2 + right**2 < c:
                left += 1
            else:
                return True
        return False