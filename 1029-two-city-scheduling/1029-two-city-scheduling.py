class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        length = len(costs)
        
        for cost in costs:
            cost.append(abs(cost[0]- cost[1]))
            
        costs.sort(key=lambda x: x[2])
        
        count = [0,0]
        total = 0
        while costs:
            cost = costs.pop()
            
            if (cost[0] < cost[1] and count[0] < length//2) or (count[1] >= length//2):
                total += cost[0]
                count[0] += 1
            else:
                total += cost[1]
                count[1] += 1
    
        return total