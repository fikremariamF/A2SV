class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0
        @cache
        def steps(curr, copy, isCopy):
            if curr == n :
                return 0
            if curr > n:
                return n + 1
            if isCopy:
                return steps(curr + copy, copy ,False) + 1
            else:
                path1 = steps(curr, curr, True)
                path2 = steps(curr + copy, copy, False)
                return min(path1, path2) + 1
        
        return steps(1, 1, True) + 1
