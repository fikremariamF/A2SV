class Solution:
    def findComplement(self, num: int) -> int:
        temp = num
        output = []
        while num  > 1:
            output.append(num % 2)
            num = num//2
        output.append(num)
        for k in range(len(output)):
            temp ^= (1<<k)
        return temp