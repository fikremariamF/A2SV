class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = ""
        carry = 0

        a, b = (a, b) if len(a) >= len(b) else (b, a)

        b = b.zfill(len(a))

        for i in range(len(a) - 1, -1, -1):
            sum = int(a[i]) + int(b[i]) + carry

            if sum >= 2:
                carry = 1
                sum -= 2
            else:
                carry = 0

            result = str(sum) + result

        if carry:
            result = "1" + result

        return result

            