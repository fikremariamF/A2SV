class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0

        n = len(prices)
        leftProfit = [0] * n
        rightProfit = [0] * n

        min_price_left = prices[0]
        for i in range(1, n):
            leftProfit[i] = max(leftProfit[i-1], prices[i] - min_price_left)
            min_price_left = min(min_price_left, prices[i])

        max_price_right = prices[n-1]
        for i in range(n-2, -1, -1):
            rightProfit[i] = max(rightProfit[i+1], max_price_right - prices[i])
            max_price_right = max(max_price_right, prices[i])

        max_combined_profit = 0
        for i in range(n):
            max_combined_profit = max(max_combined_profit, leftProfit[i] + rightProfit[i])

        return max_combined_profit




