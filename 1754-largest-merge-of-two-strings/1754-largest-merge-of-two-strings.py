class Solution:
    # def largestchecker:
    def largestMerge(self, word1: str, word2: str) -> str:
        ptr1, ptr2 = 0, 0
        word1 = list(word1)
        word2 = list(word2)
        output = []
        while ptr1 < len(word1) and ptr2 < len(word2):
            if word1[ptr1:] > word2[ptr2:]:
                output.append(word1[ptr1])
                ptr1 += 1
            else:
                output.append(word2[ptr2])
                ptr2 += 1
        output.extend(word1[ptr1:])
        output.extend(word2[ptr2:])
        return "".join(output)