class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        total = [0 for _ in range(len(cost))]
        total[-1] = cost[-1]
        total[-2] = cost[-2]
        for idx in range(len(cost) - 3, -1, -1):
            total[idx] = cost[idx] + min(total[idx + 1], total[idx + 2])
        print(total)
        return min(total[0], total[1])