class Solution:
    def maxProduct(self, words: List[str]) -> int:
        bits = []
        for word in words:
            num = 0
            for letter in word:
                num |= (1 << (ord(letter) - 96))
            bits.append(num)
        output = 0
        for i in range(len(bits)):
            for j in range(i, len(bits)):
                if bits[i] & bits[j] == 0:
                    output = max(len(words[i]) * len(words[j]), output)
                    
        return output