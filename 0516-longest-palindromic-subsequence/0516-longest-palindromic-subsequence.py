class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        @lru_cache(None)
        def dfs(l, r):
            if l > r:
                return 0
            elif l == r:
                return 1
            
            if s[l] == s[r]:
                return dfs(l + 1, r - 1) + 2
                
            return max(dfs(l + 1, r), dfs(l, r - 1))
        return dfs(0, len(s) - 1)
                