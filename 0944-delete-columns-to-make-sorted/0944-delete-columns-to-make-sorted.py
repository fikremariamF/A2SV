class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        popped = 0
        for col in range(len(strs[0])):
            val = 0
            for row in range(len(strs)):
                # print(val, ord(strs[row][col]), strs[row][col])
                if ord(strs[row][col]) < val:
                    popped += 1
                    break
                val = ord(strs[row][col])
        return popped