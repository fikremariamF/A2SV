class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        counts = [0 for char in s]
        letters = [ord(char) for char in s]
        
        # add -1 if shifts[2] is 0 else add one to the index
        for shift in shifts:
            if shift[2] == 0:
                counts[shift[0]] -= 1
                if shift[1] + 1 < len(s):
                    counts[shift[1] + 1] += 1
            else:
                counts[shift[0]] += 1
                if shift[1] + 1 < len(s):
                    counts[shift[1] + 1] -= 1
        letters[0] += counts[0]
        # calculate the prefix sum
        for idx in range(1 , len(counts)):
            counts[idx] += counts[idx -1]
            letters[idx] += counts[idx]
        
        final = []
        for asci in letters:
            asci = asci - 97
            asci = asci % 26
            asci = asci + 97
            final.append(chr(asci))
        return "".join(final)