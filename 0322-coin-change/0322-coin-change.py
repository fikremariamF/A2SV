class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        steps = [0 for _ in range(amount + 1)]
        
        for idx in range(1,amount + 1):
            val = float("inf")
            for coin in coins:
                if idx - coin >= 0:
                    val = min(val,steps[idx - coin])
            steps[idx] = val + 1
            
        if steps[-1] == float('inf'):
            return -1
        return steps[-1]