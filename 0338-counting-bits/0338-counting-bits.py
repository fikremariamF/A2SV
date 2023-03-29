class Solution:
    def countBits(self, n: int) -> List[int]:
        output = []
        for idx in range(n + 1):
            count = 0
            while idx > 0:
                count += ((idx)&1)
                idx >>= 1
            output.append(count)
        return output