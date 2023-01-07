class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        squares = [2 ** n for n in range(22)]
        # print(squares)
        counts = Counter(deliciousness)
        pairs = 0
        for index in range(len(deliciousness)):
            for square in squares:
                val = square - deliciousness[index]
                if val in counts:
                    if val == deliciousness[index]:
                        pairs += (counts[val] - 1)
                    else:
                        pairs += (counts[val])
        return (pairs//2) % ((10**9)+7)