class Solution:
    def countArrangement(self, n: int) -> int:
        @lru_cache(None)
        def dfs(i,mask):
            if i == n+1:
                return 1
            
            total = 0

            for j in range(n):
                if mask&(1<<j) == 0 and ((j+1)%i == 0 or i%(j+1) == 0):
                    total += dfs(i+1,mask|(1<<j))

            return total

        return dfs(1,0)
