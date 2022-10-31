class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        i = 0
        k = k % sum(chalk)
        while k >= chalk[i]:
            k -= chalk[i]
            i += 1
            if i == len(chalk):
                i = 0
        return i
