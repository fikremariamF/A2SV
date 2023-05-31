class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        steps = dict()
        
        def dp(num):
            if num < 0:
                return float("inf")
            elif num == 0:
                return 0
            val = float("inf")
            for coin in coins:
                if num - coin in steps:
                    val = min(val, steps[num - coin])
                else:
                    val = min(val, dp(num - coin))
            steps[num] = val + 1
            return val + 1
        output = dp(amount)
        # print(steps)
        if output == float("inf"):
            return -1
        return output