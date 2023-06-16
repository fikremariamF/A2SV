class Solution:
    def solve(self, i, bought, fee, n, prices, dp):
        if i == n:
            return 0
        if (i, bought) in dp:
            return dp[(i, bought)]
        
        sell, buy = 0, 0
        if bought:
            sell = max(self.solve(i+1, 0, fee, n, prices, dp)+prices[i]-fee, self.solve(i+1, bought, fee, n, prices, dp))
        else:
            buy = max(self.solve(i+1, 1, fee, n, prices, dp)-prices[i], self.solve(i+1, bought, fee, n, prices, dp))
        
        dp[(i, bought)] = max(sell, buy)
        return dp[(i, bought)]
    
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        dp = dict()
        return self.solve(0, 0, fee, n, prices, dp)
        