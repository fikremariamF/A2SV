class Solution:
    def climbStairs(self, n: int, i = 0, memo = defaultdict()) -> int:
        if i == 0:
            memo = defaultdict()
        total = 0
        if i == n:
            total += 1
        elif i > n:
            total += 0
        else:
            if i + 1 in memo:
                total += memo[i+1]
            else:
                total += self.climbStairs(n, i + 1, memo)
            if i + 2 in memo:
                total += memo[i+2]
            else:
                total += self.climbStairs(n, i + 2, memo)
        memo[i] = total

        return total
                
        