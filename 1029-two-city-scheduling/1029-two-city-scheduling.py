class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        length = len(costs)
        for cost in costs:
            cost.append(abs(cost[0]- cost[1]))
        # print(costs)
        costs.sort(key=lambda x: x[2])
        # print(costs)
        count = [0,0]
        total = 0
        while costs:
            cost = costs.pop()
            # print(cost, count)
            if (cost[0] < cost[1] and count[0] < length//2) or (count[1] >= length//2):
                # print("in")
                total += cost[0]
                count[0] += 1
            else:
                # print("out")
                total += cost[1]
                count[1] += 1
        # print(total)
        return total