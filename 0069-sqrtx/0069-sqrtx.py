class Solution:
    def mySqrt(self, x: int) -> int:
        # arr = [i for i in range((x//2) + 1)]
        # print(arr)
        left, right = 0, x
        if x == 1:
            return 1
        while left <= right:
            mid = (left + right)//2
            # print(left, right, mid)
            if mid ** 2 > x:
                right = mid - 1
            elif mid * mid < x and (mid +1) ** 2 <= x:
                left = mid + 1
            else:
                return mid
        