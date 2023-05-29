class Solution:
    def tribonacci(self, n: int) -> int:
        pred = [0, 1, 1]
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        def sequence(i):
            # print(pred)
            pred.append(pred[-1] + pred[-2] + pred[-3])
            if i != n:
                sequence(i + 1)
            return
        sequence(3)
        return pred[-1]
        