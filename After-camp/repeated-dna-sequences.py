class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        sequences = defaultdict(int)
        repeated_sequences = []

        for i in range(len(s) - 9):
            seq = s[i:i+10]
            sequences[seq] += 1
            if sequences[seq] == 2:
                repeated_sequences.append(seq)

        return repeated_sequences