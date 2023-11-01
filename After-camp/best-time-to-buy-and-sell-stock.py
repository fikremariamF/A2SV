class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        soln = [0]
        maxx = prices[-1]
        for idx in range(len(prices)-1, -1, -1):
            maxx = max(maxx, prices[idx])
            soln.append(maxx - prices[idx])
        return max(soln)